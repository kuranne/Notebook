#!/usr/bin/env python3
import os
import sys
import re
import argparse
import subprocess

EMOJI_PATTERN = re.compile(
    r'('
    r'[\U0001F600-\U0001F64F]'
    r'|[\U0001F300-\U0001F5FF]'
    r'|[\U0001F680-\U0001F6FF]'
    r'|[\U0001F1E6-\U0001F1FF]{2}'
    r'|[\U0001F900-\U0001F9FF]'
    r'|[\U0001FA00-\U0001FAFF]'
    r'|[\U0001F7E0-\U0001F7EB]'
    r'|[\u2600-\u26FF]'
    r'|[\u2700-\u27BF]'
    r'|[\u231A\u231B\u23E9-\u23EC\u23F0\u23F3]'
    r'|[\u2B50\u2B55]'
    r')'
)

# Detect bilingual glosses like English followed by Thai in parentheses or vice versa
BILINGUAL_PAREN_PATTERN = re.compile(
    r'([a-zA-Z]{3,}\s*\([ก-๙\s]+\)|[ก-๙]{3,}\s*\([a-zA-Z\s]+\))'
)

# Detect deprecated body navigation callouts in vault notes
NAV_CALLOUT_PATTERN = re.compile(r'>\s*\[!info\]\s*Navigation:', re.IGNORECASE)

IGNORE_DIRS = {
    '.git', '.cache', '.system_generated', 'node_modules', 'vendor',
    '.venv', 'venv', 'build', 'dist', '.agents/log', '.agent/log', '.agents/scripts'
}

def lint_file(file_path, is_meta_rule=False):
    errors = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        return [f"Unable to read file: {e}"]

    in_frontmatter = False

    for idx, line in enumerate(lines, start=1):
        # 1. Emoji check (strict for all files)
        emojis = EMOJI_PATTERN.findall(line)
        if emojis:
            errors.append(f'Line {idx}: Forbidden emoji characters: {"".join(emojis)}')

        # Meta-rule files (.agents/rules/ and AGENTS.md) describe prohibitions, so skip self-matching patterns
        if not is_meta_rule:
            # 2. Bilingual parentheticals check
            bilingual = BILINGUAL_PAREN_PATTERN.findall(line)
            if bilingual:
                errors.append(f'Line {idx}: Forbidden bilingual parenthetical gloss: {bilingual}')

            # 3. Legacy body navigation callouts check
            if NAV_CALLOUT_PATTERN.search(line):
                errors.append(f'Line {idx}: Deprecated body navigation callout found. Use YAML class/parent instead.')

        # 4. Frontmatter wikilinks check
        if idx == 1 and line.strip() == '---':
            in_frontmatter = True
            continue
        elif in_frontmatter and line.strip() == '---':
            in_frontmatter = False
            continue

        if in_frontmatter:
            if '[[' in line and ']]' in line:
                errors.append(f'Line {idx}: Wikilink found in YAML frontmatter. Frontmatter must use plain strings.')

    return errors

def main():
    parser = argparse.ArgumentParser(description="Lint CSTU40 files for rule compliance.")
    parser.add_argument('--path', default=None, help='Target directory or file to lint')
    parser.add_argument('--staged', action='store_true', help='Lint only git staged files')
    parser.add_argument('--changed', action='store_true', help='Lint git changed/uncommitted files')
    args = parser.parse_args()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(current_dir))

    target_files = []
    scan_exts = ('.md', '.txt', '.py', '.c', '.cpp', '.java', '.h')

    if args.staged or args.changed:
        cmd = ['git', '-C', repo_root, 'diff', '--name-only']
        if args.staged:
            cmd.append('--cached')
        res = subprocess.run(cmd, capture_output=True, text=True)
        for rel in res.stdout.strip().split('\n'):
            if rel and rel.endswith(scan_exts):
                target_files.append(os.path.join(repo_root, rel))
    elif args.path:
        target_path = os.path.abspath(args.path)
        if os.path.isfile(target_path):
            target_files.append(target_path)
        else:
            for root, dirs, files in os.walk(target_path):
                dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not any(ign in os.path.join(root, d) for ign in IGNORE_DIRS)]
                for f in files:
                    if f.endswith(scan_exts):
                        target_files.append(os.path.join(root, f))
    else:
        for root, dirs, files in os.walk(repo_root):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not any(ign in os.path.join(root, d) for ign in IGNORE_DIRS)]
            for f in files:
                if f.endswith(scan_exts):
                    target_files.append(os.path.join(root, f))

    failed_files = 0
    for fp in target_files:
        is_meta_rule = ('.agents/rules' in fp or fp.endswith('AGENTS.md'))
        errs = lint_file(fp, is_meta_rule=is_meta_rule)
        if errs:
            failed_files += 1
            rel = os.path.relpath(fp, repo_root)
            print(f'[FAIL] {rel}')
            for e in errs:
                print(f'   {e}')

    print(f'\nLint complete: {len(target_files)} files scanned, {failed_files} failed.')
    if failed_files > 0:
        sys.exit(1)
    else:
        print('[PASS] All checked files conform to CSTU40 rules.')
        sys.exit(0)

if __name__ == '__main__':
    main()

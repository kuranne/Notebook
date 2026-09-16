# Verification & Quality Assurance

## 1. Pre-Commit Verification Gate
Agents must run automated verification before finalizing tasks or committing changes:
1. Lint Validation: Run `.agents/scripts/lint_vault.py` against changed files.
2. Zero-Emoji Check: Confirm 0 emoji code points.
3. Language Check: Confirm no parenthetical translation suffixes.
4. Schema Check: Confirm frontmatter contains required fields (`class`, `parent`, `type`) with pure string values and zero wikilinks.
5. Tree Linking Check: Confirm no legacy breadcrumb callouts (`> [!info] Navigation:`) and no unverified horizontal cross-links.

## 2. Command Execution
```bash
python3 .agents/scripts/lint_vault.py --check
```
If violations are detected, resolve all lint errors before committing.

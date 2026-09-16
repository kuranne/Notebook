# Notebook Vault - Agent Operations Manual

## 1. Overview & Core Mission
Master operations manual and quality standards for the Obsidian Notebook vault.
The vault houses academic repositories, personal notes, study templates, and curriculum submodules (including `University/CSTU40`).

Agents operating within this vault maintain documentation consistency, clean graph topology, and strict styling across all notes.

---

## 2. Directory Architecture & Modular Customizations

```
.agents/
├── rules/
│   ├── 01-style-language.md      # Zero-emoji mandate, single-language policy, high density
│   ├── 02-logging-git.md         # Commit-before-logging workflow, terse log schema, rotation
│   └── 03-verification.md        # Pre-commit gate via lint_vault.py
├── scripts/
│   └── lint_vault.py             # Automated linter for emojis, glosses, schemas, callouts
├── skills/
│   ├── obsidian-expert-skill.md  # Obsidian markdown, callouts, and Dataview authoring
│   ├── latex-math-skill.md       # LaTeX and MathJax mathematical typesetting
│   └── mermaid-diagram-skill.md  # Mermaid diagrams, flowcharts, and architecture models
└── AGENTS.md                     # Master operations manual
```

---

## 3. Core Vault Directives

### 3.1 Style & Language
- Zero emojis across all files, notes, rules, and commits.
- Strict single language per context. English is required for technical notes; Thai is reserved for humanities and Thai-taught courses.
- No bilingual parenthetical translations (e.g. `Term (Translation)` or `Word (คำแปล)`).
- High density, concise technical prose.
- See detailed rules in [01-style-language.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/.agents/rules/01-style-language.md).

### 3.2 Git Commit & Audit Logging
- Commit-before-logging: Always stage and commit mutated files to Git before appending to changelog.
- Extract short commit hash (`git rev-parse --short HEAD`) and include it in log entries.
- Maintain session logs in `.agent/log/YYYY-MM-DD_<agent>.log` and repo log in `.agents/log/changelog.log`.
- Log rotation: Compress via `tar -cJf` when changelog entries reach >= 16; purge oldest archives when archive count reaches >= 16.
- See log specifications in [02-logging-git.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/.agents/rules/02-logging-git.md).

### 3.3 Automated Pre-Commit Verification
- Run validation before any commit or task completion:
  `python3 .agents/scripts/lint_vault.py`
- Ensure 0 errors for emojis, bilingual glosses, invalid schemas, or deprecated navigation callouts.
- See verification protocol in [03-verification.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/.agents/rules/03-verification.md).

---

## 4. Submodule Governance
Domain-specific curriculum structures, note hierarchies, and directory layouts are maintained independently within their respective submodules:
- **CSTU40 (`University/CSTU40`)**: Maintains its 5-tier note hierarchy, course directory archetype, and YAML frontmatter schemas under `University/CSTU40/.agents/`.

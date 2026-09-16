# CSTU40 Agent System Documentation

## 1. Overview & Core Mission
Central academic knowledge base and coursework repository for Computer Science, Thammasat University (Cohort 40).
Agents assist with summarization, structural organization, and relational knowledge management while maintaining repository integrity.

Agents autonomously maintain configurations under `.agent/` and `.agents/`.

---

## 2. Directory Architecture & Modular Customizations

```
.agents/
├── rules/
│   ├── 01-style-language.md      # Zero-emoji mandate, single-language policy, high density
│   ├── 02-tree-hierarchy.md      # Strict top-down tree, parent-child traversal, no random cross-links
│   ├── 03-frontmatter-schema.md  # Tiered YAML schemas (class, parent, type), zero wikilinks
│   ├── 04-workspace-structure.md # Archetype layout, course rosters, copyright protection
│   ├── 05-logging-git.md         # Commit-before-logging workflow, terse log schema, rotation
│   └── 06-verification.md        # Pre-commit gate via lint_vault.py
├── scripts/
│   └── lint_vault.py             # Automated linter for emojis, glosses, schemas, callouts
├── skills/
│   ├── obsidian-expert-skill.md  # Obsidian markdown, callouts, and Dataview authoring
│   ├── latex-math-skill.md       # LaTeX and MathJax mathematical typesetting
│   └── mermaid-diagram-skill.md  # Mermaid diagrams, flowcharts, and architecture models
└── AGENTS.md                     # Master operations manual
```

---

## 3. Core Operational Directives

### 3.1 Style & Language
- Zero emojis across all files, notes, rules, and commits.
- Strict single language per context. English is required for technical and CS courses; Thai is reserved for humanities and Thai-taught courses.
- No bilingual parenthetical translations (e.g. `Term (Translation)` or `Word (คำแปล)`).
- See detailed rules in [01-style-language.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/University/CSTU40/.agents/rules/01-style-language.md).

### 3.2 Tree Hierarchy & Linking
- Strict tree hierarchy: Root (`README.md`) -> Year -> Semester -> Course Hub -> Leaf Note.
- Parent notes link down to immediate children in note bodies.
- Child notes declare parent in YAML frontmatter (`parent: "Parent Note"`).
- Sibling/leaf notes must NOT cross-link horizontally unless explicitly citing or depending on specific content from another file.
- Deprecate and remove legacy body breadcrumb callouts (`> [!info] Navigation:`).
- See detailed rules in [02-tree-hierarchy.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/University/CSTU40/.agents/rules/02-tree-hierarchy.md).

### 3.3 YAML Frontmatter Schemas
- Every note requires valid YAML frontmatter.
- Mandatory fields for leaf notes: `class` (e.g. `CS261`), `type` (e.g. `lecture`, `lab`), `title`, `parent` (e.g. `"CS261"`).
- Plain YAML strings only; zero `[[wikilinks]]` in frontmatter.
- See full schemas in [03-frontmatter-schema.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/University/CSTU40/.agents/rules/03-frontmatter-schema.md).

### 3.4 Workspace Archetype & Assets
- Course directory layout: `Year {N}/Semester {N}/{Course Code} - {Course Name}/[Assignments, Labs, Lectures, Assets, Private]`.
- Lecture code parsing: Ignore non-code lecture files; parse only source code (`.c`, `.cpp`, `.java`, `.py`, `.ipynb`, `.arm`, `.s`, `.h`).
- Copyright protection: Place official slides and syllabi in `<Course>/Private/Docs/` (`**/[Pp]rivate/**` gitignored).
- Zero file duplication; use symlinks or hard links (`ln -s` / `ln`).
- See detailed layout in [04-workspace-structure.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/University/CSTU40/.agents/rules/04-workspace-structure.md).

### 3.5 Git Commit & Audit Logging
- Commit-before-logging: Always stage and commit mutated files to Git before appending to changelog.
- Extract short commit hash (`git rev-parse --short HEAD`) and include it in log entries.
- Maintain session logs in `.agent/log/YYYY-MM-DD_<agent>.log` and repo log in `.agents/log/changelog.log`.
- Log rotation: Compress via `tar -cJf` when changelog entries reach >= 16; purge oldest archives when archive count reaches >= 16.
- See log specifications in [05-logging-git.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/University/CSTU40/.agents/rules/05-logging-git.md).

### 3.6 Automated Pre-Commit Verification
- Run validation before any commit or task completion:
  `python3 .agents/scripts/lint_vault.py --check`
- Ensure 0 errors for emojis, bilingual glosses, invalid schemas, or deprecated navigation callouts.
- See verification protocol in [06-verification.md](file:///Users/kuranne/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/Notebook/University/CSTU40/.agents/rules/06-verification.md).

---

## 4. Operational Boundaries

- **Required**:
  - Run `.agents/scripts/lint_vault.py` before finalizing commits.
  - Adhere to single language per heading; no parenthetical dual-language glosses.
  - Store protected academic handouts under `Private/Docs/`.
  - Maintain links strictly through parent hubs; horizontal cross-links require explicit content dependency.
  - Record short commit SHA in log entries.
- **Prohibited**:
  - Never insert Unicode emojis into any file.
  - Never place `[[wikilinks]]` inside YAML frontmatter.
  - Never use legacy body breadcrumbs (`> [!info] Navigation:`).
  - Never duplicate files across directories; use symlinks.
  - Never modify or delete `.git/` internals.

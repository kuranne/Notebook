---
name: obsidian-expert
description: >-
  Provides expert guidance on formatting, structuring, and maintaining Obsidian notes.
  Use this skill whenever working with markdown files inside an Obsidian vault, writing frontmatter properties,
  creating visual callouts, generating Dataview queries, or writing Mermaid diagrams and mathematical formulas.
when_to_use: |
  - User wants to edit, create, or refactor notes in an Obsidian markdown vault
  - User asks to structure YAML frontmatter, organize properties, or set up note templates
  - User wants to formulate Dataview tables, list views, or task queries
  - User asks to draw system flows using Mermaid diagrams or format LaTeX equations
license: MIT
metadata:
  author: Gemini Notebook
  version: 1.1.0
---

# Obsidian Expert AI Agent Skill

## Purpose
This skill provides an authoritative, complete, and spec-valid instruction set for writing, formatting, and structuring notes inside an Obsidian vault. It ensures coding agents respect visual, programmatic, and relational specifications of the Obsidian environment, ensuring maximum readability, accurate metadata, and flawless rendering.

---

## Modular Sub-Skills in `.agents/skills/`
For specialized in-depth reference guides and advanced syntax rules, consult:
- **`latex-math-skill.md`**: Complete reference for mathematical formulas, calculus, linear algebra, probability, matrices, and MathJax syntax.
- **`mermaid-diagram-skill.md`**: Complete specification for Flowcharts, Sequence diagrams, Class diagrams, ERDs, State machines, and Git graphs.

---

## Core Obsidian Specifications

### 1. Properties & Frontmatter (v1.4+)
Obsidian uses YAML frontmatter flanked by triple dashes (`---`) at the absolute top of the note to define metadata. Since version 1.4, Obsidian displays these as typed fields in the UI. Agents must follow these rules:
- **Strict Typing**: Ensure field values conform to Obsidian's property types:
  - `text`: Simple strings (e.g., `author: "David Thomas"`)
  - `number`: Numeric values (e.g., `rating: 5`)
  - `date`: ISO dates (`YYYY-MM-DD` or `YYYY-MM-DDTHH:mm`) (e.g., `due: 2026-06-15`)
  - `checkbox`: Boolean values (`true` or `false`) (e.g., `archived: false`)
  - `list`: YAML sequences (e.g., `tags: [projects, work]` or standard YAML bulleted array)
- **Key Consistency**: Never introduce duplicate or near-duplicate property keys (e.g., use either `due_date` or `due`, but never both). Maintain casing conventions across all notes of a given type.
- **YAML Safety**: Always wrap string values containing colons `:`, list markers, or YAML special characters in double quotes to prevent silent parsing failures.

### 2. Wikilinks & Embeds
To build a highly integrated knowledge graph, use Obsidian's wikilink syntax:
- **Standard Link**: `[[Note Name]]` links to another note in the vault.
- **Link Alias**: `[[Note Name|Display Label]]` overrides the shown link text.
- **Heading Links**: `[[Note Name#Section Title]]` targets a specific heading in the note.
- **Block Links**: `[[Note Name#^block-id]]` targets a specific block marked with a caret symbol (e.g., `^block-id`).
- **Transclusion / Embeds**: Use `![[Note Name]]` to embed and render another note's content inline. This can be combined with headings `![[Note Name#Section Title]]`.

### 3. Visual Callouts
Callouts are rendered as styled blocks with custom icons. They can be collapsible/foldable to manage information density.
- **Collapsible Syntax**:
  - `> [!type]- Title` renders a callout that is **collapsed** (initially closed) by default.
  - `> [!type]+ Title` renders a callout that is **expanded** (initially open) by default.
- **The 12 Core Callout Types**:
  1. `note`: Default callout for miscellaneous notes.
  2. `abstract` / `summary` / `tldr`: Executive summaries and key takeaways.
  3. `info`: Informational details and contextual background.
  4. `todo`: Task lists and action items.
  5. `tip` / `hint` / `important`: Helpful advice, shortcuts, and key points.
  6. `success` / `check` / `done`: Positive results and completed actions.
  7. `question` / `help` / `faq`: Inquiries, help requests, and frequently asked questions.
  8. `warning` / `caution` / `attention`: Warnings about potential issues.
  9. `failure` / `fail` / `missing`: Negative results and missing requirements.
  10. `danger` / `error`: High-severity issues and errors.
  11. `bug`: Software bugs and system defects.
  12. `example`: Concrete examples and use cases.
  13. `quote` / `cite`: Direct quotes and citations.
- **Nesting Callouts**: To nest a callout inside another, prepend an additional blockquote character `>` to the nested callout's lines. Ensure correct indentation to prevent rendering breaks.

### 4. Dataview Queries
The Dataview community plugin enables dynamic querying of note frontmatter and tags. Queries are fenced using ````dataview` blocks.
- **Core Commands**:
  - `TABLE`: Displays a table of properties.
  - `LIST`: Displays a simple list of matching notes.
  - `TASK`: Displays incomplete or complete tasks inside notes.
  - `CALENDAR`: Renders note dates in a monthly view.
- **Logical clauses**:
  - `FROM`: Scopes the query to tags (`#tag`) or folders (`"folder/path"`).
  - `WHERE`: Applies filters based on properties (e.g., `WHERE status = "active" AND priority = "high"`).
  - `SORT`: Orders results (e.g., `SORT due ASC`).
- **Syntax Conventions**:
  - Property keys are case-sensitive.
  - String comparisons must use double quotes.
  - Null checks should be performed using `!= null` or `!= undefined`.

### 5. Mermaid Diagrams (See `mermaid-diagram-skill.md` for full spec)
Obsidian natively supports Mermaid diagrams to visualize concepts, flows, and relationships.
- **Fenced Blocks**: Fenced using ````mermaid` blocks.
- **Key Diagram Types**:
  - Flowcharts: `flowchart TD` (Top-Down) or `flowchart LR` (Left-to-Right).
  - Sequence Diagrams: `sequenceDiagram` for message flows.
  - Class Diagrams: `classDiagram` for OOP architectures.
  - Entity-Relationship: `erDiagram` for relational database schemas.
  - State Diagrams: `stateDiagram-v2` for state machines.
  - Git Graphs: `gitGraph` for version control timelines.

### 6. MathJax & LaTeX Notation (See `latex-math-skill.md` for full spec)
LaTeX mathematical expressions are rendered natively in Obsidian.
- **Inline Math**: Wrapped in single dollar signs `$E = mc^2$`. Do not leave spaces between the dollar signs and the math content (e.g., write `$x_2$` not `$ x_2 $`).
- **Block Math**: Wrapped in double dollar signs `$$` on separate lines:
  ```latex
  $$
  f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi) e^{2 \pi i \xi x} \, d\xi
  $$
  ```

---

## Operational Workflow

When tasked with creating, editing, or organizing notes inside an Obsidian vault, follow this step-by-step workflow:

1. **Vault Schema Assessment**:
   - Check if the vault has established templates or a directory structure.
   - Scan existing files in `/workspace/knowledge/` or notes in the same folder to match casing, keys, and tags.

2. **Template Application**:
   - Start note creation with a structured YAML frontmatter block.
   - Separate metadata from content: place identifiers, dates, status, and tags in frontmatter, and keep the main text body clear of administrative clutter.

3. **Writing and Structuring Content**:
   - Organize notes around single, atomic topics (Zettelkasten method).
   - Use headings logically (`#`, `##`, `###`) to allow target-rich links and foldable sections.
   - Utilize Visual Callouts to separate meta-discussions, alerts, or examples from the main body.
   - Embed Mermaid flowcharts to clarify processes, architectures, or life cycles.
   - Embed MathJax block quotes for mathematical or statistical models.

4. **Interlinking Notes**:
   - Explicitly link new notes to existing vault notes using `[[Note Name]]` or alias formats.
   - If referencing specific sections, append the heading tag: `[[Note Name#Section Heading]]`.
   - Update index pages or write Dataview queries (such as a dynamic list or table) to auto-surface the newly created notes in the folder.

5. **Sanity Check & Metadata Hygiene**:
   - Review the note's frontmatter to ensure all key properties are filled, consistent, and correctly typed.
   - Clean up any unused or redundant keys.
   - Ensure Mermaid blocks compile without syntax errors.

---

## Boundaries & Anti-Patterns

- **Always do**: Start note creation with a structured YAML frontmatter block. Use standard Obsidian wikilinks (`[[Note Name]]`) for internal vault linking. Use exact lower-case callout type identifiers (e.g., `[!warning]`, not `[!Warning]`).
- **Ask first**: Before creating new tags or metadata keys that do not exist in the vault's current schema. Before refactoring a highly-linked core index or map of content note.
- **Never do**:
  - **Never use relative paths** for note linking (e.g., `[My Note](../folder/My%20Note.md)`) if Obsidian's wikilink format is active. This breaks the local graph visualization.
  - **Never use proprietary comment syntax** (e.g., `%% hidden comment %%`) in documents that might be processed or viewed outside of Obsidian, as this leaks private annotations in standard markdown.
  - **Never write unquoted special characters** (like colons `:`) in property string values, as this breaks the YAML parsing engine and causes Obsidian to ignore the note's frontmatter entirely.
  - **Never use inconsistent naming conventions** for properties (e.g., mixing `due-date`, `dueDate`, and `due_date`) inside the same vault, as this renders Dataview tables blank or half-empty.

---

## Self-Validation Heuristics

Before finalizing your work, programmatically or textually check:
1. **Frontmatter Integrity**: Does the YAML block begin and end with exactly `---`? Are all string values containing `:` or other special symbols properly enclosed in double quotes?
2. **Dataview Check**: Are property keys named exactly as expected in the query? (Remember, Dataview is case-sensitive).
3. **Wikilink Verification**: Do all `[[Note Name]]` links target valid, existing files or are they intended to be placeholder red links?
4. **Callout Rendering**: Are all callout blocks correctly prepended with `>` and a space? Is the syntax exactly `> [!type]` with the correct type identifier?
5. **LaTeX Rendering**: Are all single-dollar inline equations formatted with no space adjacent to the `$`?
6. **Mermaid Validation**: Are all node labels containing special characters enclosed in double quotes `["..."]`?

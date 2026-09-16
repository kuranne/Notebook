# Tree Hierarchy & Linking Policy

## 1. Tree Hierarchy Model
The repository knowledge base is structured as a strict top-down tree:
- Level 0 (Root): `README.md`
- Level 1 (Year): `Year {N}/Year {N}.md`
- Level 2 (Semester): `Year {N}/Semester {N}/Year {N} Semester {N}.md`
- Level 3 (Course Hub): `Year {N}/Semester {N}/{Course Code} - {Course Name}/Lectures/{Course Code}.md`
- Level 4 (Leaf Notes): Topic notes, lecture summaries, lab guides, assignment reports.

## 2. Strict Downward & Upward Traversal
- Parent notes link down to their immediate children in the markdown body (e.g. tables of contents, Dataview lists).
- Child notes link up to their parent via YAML frontmatter `parent: "Parent Name"`.
- Standard navigation must always traverse via the immediate Parent.

## 3. Horizontal Cross-Linking Constraints
- Arbitrary cross-linking between sibling notes or across branches is prohibited.
- Explicit Dependency Exception: Horizontal links (`[[Target Note]]` or `[[Target Note|Label]]`) are permitted ONLY when a note explicitly cites, imports, or builds upon specific content from another file (e.g. citing a theorem, referencing an architecture diagram, or extending an algorithm).
- Graph edges must reflect true knowledge dependency, not casual topic association.

## 4. Deprecation of Body Breadcrumb Navigators
- In-body breadcrumb callouts (e.g. `> [!info] Navigation: [[...]] > [[...]]`) are strictly prohibited.
- Hierarchy is maintained purely through YAML frontmatter `class` and `parent` fields combined with Parent Hub listings.

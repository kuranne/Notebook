# Workspace Structure & Assets

## 1. Directory Archetype
All courses adhere to the uniform directory structure:
```
Year {N}/Semester {N}/{Course Code} - {Course Name}/
├── Assignments/  # Submissions, homework tasks, problem sets
├── Labs/         # Weekly lab exercises, runnable source implementations
├── Lectures/     # Hub note ({Course Code}.md), lecture notes, class code files
├── Assets/       # Course diagrams, schema images, datasets
└── Private/      # Protected course materials (Gitignored)
    └── Docs/     # Official lecture slides, syllabi, instructor PDFs
```

## 2. Course Rosters
- Year 1 Sem 1: CS100, CS101, CS102, LAS101, TU107, TU109
- Year 1 Sem 2: CS111, EL295, TU100, TU101, TU106, TU108
- Year 2 Sem 1: CS213, CS221, CS240, CS261, HS369, PY252, ST329

## 3. Lecture Folder Parsing Constraints
- When parsing `Lectures/`, ignore miscellaneous presentations, handouts, or notes UNLESS they are class code source files (`.c`, `.cpp`, `.java`, `.py`, `.ipynb`, `.arm`, `.x86`, `.s`, `.h`).
- Miscellaneous non-code lecture files are out of programmatic scope.

## 4. Protected Assets & Copyright
- All university handouts, slides, and instructor materials must be placed in `<Course>/Private/Docs/`.
- The pattern `**/[Pp]rivate/**` is gitignored to protect institutional intellectual property.

## 5. Zero-Waste Duplication Policy
- Never create duplicate files across folders.
- Cross-reference shared resources via standard Unix symbolic or hard links (`ln -s` or `ln`).

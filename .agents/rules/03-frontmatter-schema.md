# YAML Frontmatter Specification

## 1. General Frontmatter Rules
- Every Markdown note must start with YAML frontmatter enclosed in `---`.
- Frontmatter values must be standard YAML types: strings, numbers, booleans, dates, or sequences.
- STRICTLY NO `[[wikilinks]]` in frontmatter. Frontmatter fields are metadata attributes, not graph relation edges.

## 2. Schema by Hierarchy Tier

### Root Index (`README.md`)
```yaml
---
type: root_index
title: Computer Science Thammasat University (Cohort 40)
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Year Index (`Year {N}.md`)
```yaml
---
type: year_index
title: Year N Overview
year: N
parent: "README"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Semester Index (`Year {N} Semester {N}.md`)
```yaml
---
type: semester_index
title: Year N Semester N Index
year: N
semester: N
parent: "Year N"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Course Hub (`{Course Code}.md`)
```yaml
---
type: course_hub
class: CS261
title: CS261 Software Engineering Hub
parent: "Year 2 Semester 1"
instructor: "Instructor Name"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Leaf Note (Lecture / Lab / Assignment)
```yaml
---
type: lecture
class: CS261
title: Software Process Models
parent: "CS261"
week: 2
tags:
  - software-engineering
  - process-models
description: Brief one-line scope summary
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

# Changelog & Git Protocol

## 1. Commit-Before-Logging Workflow
Operational traceability requires committing modifications before logging:
1. Mutate Files: Execute edits, refactoring, or file creations.
2. Git Commit: Stage and commit all mutated files:
   `git add <files>`
   `git commit -m "<action>: <terse summary>"`
3. Retrieve SHA: Extract generated commit hash:
   `git rev-parse --short HEAD`
4. Record Log: Append structured log entry with `COMMIT SHA` into:
   - Session log: `.agent/log/YYYY-MM-DD_<agent_or_task>.log`
   - Repo changelog: `.agents/log/changelog.log`

## 2. Terse Log Entry Format
```log
================================================================================
TIMESTAMP   : [ISO8601, e.g. 2026-09-15T23:30:00+07:00]
COMMIT SHA  : [Short SHA, e.g. a1b2c3d]
OPERATOR    : [agent persona, e.g. organizer.agent.md]
ACTION TYPE : [ORGANIZE | SUMMARIZE | REFACTOR | CONFIG_UPDATE | LINT]
TARGETS     :
  - [relative/path/to/file1.md]
  - [relative/path/to/file2.md]
CHANGELOG   :
  - [Terse description of changes]
  - [YAML frontmatter or links updated]
STATUS      : [SUCCESS | PARTIAL | FAIL]
ERRORS/NOTES: [None | details]
================================================================================
```

## 3. Log Compression & Rotation
- When entries in `.agents/log/changelog.log` reach or exceed 16:
  `tar -cJf .agents/log/changelog_$(date +%Y%m%dT%H%M%S).tar.xz .agents/log/changelog.log`
  Truncate or reset active log file.
- When compressed log archives reach or exceed 16, purge oldest archives.

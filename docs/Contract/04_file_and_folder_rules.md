# CHAPTER 4 — FILE AND FOLDER RULES

| Version | 1.0 |
|---------|-----|
| Status | Frozen |

---

# 4.1 Purpose

This chapter defines the mandatory rules for organizing files and folders within the Ruijie Cloud Backup Toolkit (RCBT).

The objective is to ensure the repository remains:

- Organized
- Predictable
- Scalable
- Maintainable
- Consistent across all project phases

Every file and folder shall have a clearly defined responsibility.

---

# 4.2 General Principles

The repository shall follow these principles:

- Single Responsibility Principle (SRP)
- Consistent directory structure
- Predictable file locations
- Modular organization
- Minimal coupling
- High cohesion

Files shall never serve multiple unrelated responsibilities.

---

# 4.3 Folder Organization

Folders shall be organized according to responsibility.

Each folder shall represent a logical component of the project.

Examples include:

- documentation
- source code
- configuration
- reports
- workspace
- logs
- tests
- utilities

Folders shall not become general storage locations.

---

# 4.4 File Organization

Each file shall have:

- one responsibility;
- one primary purpose;
- one logical owner;
- one expected location.

Files shall not mix unrelated functionality.

---

# 4.5 Naming Convention

Names shall be:

- descriptive;
- meaningful;
- consistent;
- lowercase;
- separated using underscores.

Avoid:

- temporary names;
- generic names;
- ambiguous abbreviations.

Examples:

Good

```
workspace_manager.py
authentication.py
api_mapping.py
backup_report.md
```

Poor

```
temp.py
new.py
backup2.py
misc.py
```

---

# 4.6 File Creation Rules

Before creating a new file, AI shall verify:

- the file does not already exist;
- the responsibility cannot be added to an existing module;
- creating a new file improves maintainability;
- the file complies with the project architecture.

Unnecessary files shall not be created.

---

# 4.7 Folder Creation Rules

New folders shall only be created when:

- a new logical responsibility exists;
- existing folders are no longer appropriate;
- architecture requires separation.

Folders shall never be created merely for convenience.

---

# 4.8 File Update Rules

AI shall determine the appropriate update strategy.

Possible actions include:

- Replace Full File
- Replace Section
- Insert Section
- Delete Section

The selected method shall minimize manual work while preserving readability.

---

# 4.9 File Replacement Rules

When replacing a file:

AI shall:

- preserve file purpose;
- preserve compatibility;
- avoid unrelated modifications;
- maintain formatting consistency.

Replacing an entire file shall only be performed when it is more practical than partial revision.

---

# 4.10 File Deletion Rules

Files shall only be deleted when:

- obsolete;
- replaced;
- deprecated;
- explicitly approved by the Project Owner.

Deletion shall never occur without evaluating project impact.

---

# 4.11 Folder Deletion Rules

Folders shall only be removed when:

- no longer required;
- fully migrated;
- approved by the Project Owner.

Deletion shall not leave orphaned references.

---

# 4.12 File Relocation Rules

Files may be relocated only when:

- architecture requires relocation;
- responsibility changes;
- maintainability improves.

Relocation shall preserve repository consistency.

---

# 4.13 Path Rules

Hardcoded paths are prohibited.

All paths shall be:

- configurable;
- portable;
- platform independent;
- maintainable.

Relative or dynamically resolved paths should be preferred whenever practical.

---

# 4.14 Repository Consistency

The repository shall remain:

- organized;
- easy to navigate;
- logically structured;
- free of redundant files;
- free of duplicate responsibilities.

Repository organization shall be preserved throughout every project phase.

---

# 4.15 Documentation Consistency

Whenever files or folders are added, removed, relocated, or renamed, related documentation shall be reviewed and updated if necessary.

Repository documentation shall accurately reflect the current project structure.

---

# 4.16 AI Responsibilities

Before modifying files or folders, AI shall verify:

- Development Contract;
- Project Architecture;
- Current Project Phase;
- Existing Repository Structure.

AI shall minimize unnecessary repository changes.

---

# 4.17 Restrictions

AI shall not:

- create unnecessary files;
- create unnecessary folders;
- duplicate responsibilities;
- violate the project architecture;
- introduce hardcoded paths;
- rename files without justification;
- relocate files without architectural reason.

---

# 4.18 Definition of Completion

A file or folder operation is considered complete only when:

- repository consistency is preserved;
- architecture remains valid;
- documentation remains accurate;
- no redundant files exist;
- no orphaned references remain;
- project maintainability is improved or preserved.

---

# 4.19 Chapter Summary

This chapter defines the mandatory rules governing file and folder management within the RCBT project.

Every modification shall:

- preserve repository consistency;
- maintain architectural integrity;
- follow the Single Responsibility Principle;
- minimize unnecessary repository changes;
- support long-term maintainability.

---

Last Review
-----------
2026-07-30

End of Document
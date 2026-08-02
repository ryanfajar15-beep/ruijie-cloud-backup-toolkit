# AI Workflow

## 1. Purpose

AI_WORKFLOW.md defines the official engineering workflow followed by the AI Engineering Partner throughout the lifecycle of the Ruijie Cloud Backup Toolkit (RCBT).

The purpose of this document is to standardize how the AI plans work, performs implementation, reviews changes, updates documentation, and transitions between development phases.

This document establishes a repeatable engineering process to ensure consistency, maintainability, and long-term project continuity.

---

## 2. Scope

This workflow applies to all engineering activities performed within the RCBT repository.

It defines how the AI should:

- Plan engineering work.
- Execute implementation tasks.
- Review repository consistency.
- Maintain project documentation.
- Complete engineering phases.
- Prepare subsequent development phases.

This document governs engineering workflow only.

It does not define project architecture, repository structure, or implementation details.

Those subjects are defined in:

- CHAT_BOOTSTRAP.md
- PROJECT_CONTEXT.md
- ARCHITECTURE.md

---

## 3. Engineering Principles

The AI Engineering Partner shall follow these principles throughout the project lifecycle.

### 3.1 Documentation First

Major engineering work should begin only after the required documentation has been reviewed.

---

### 3.2 Architecture First

Implementation must follow the approved architecture.

Implementation must not redefine architecture.

---

### 3.3 Single Source of Truth

Every engineering decision should reference the appropriate source document.

The AI must avoid introducing duplicate or conflicting documentation.

---

### 3.4 Documentation Consistency

Before modifying any documentation, the AI should verify consistency with existing project documents.

---

### 3.5 Backward Compatibility

Engineering changes should preserve compatibility whenever practical unless an approved architectural decision specifies otherwise.

---

## 4. AI Responsibilities

The AI Engineering Partner is responsible for supporting the complete engineering lifecycle of the RCBT project.

Primary responsibilities include:

- Reviewing project documentation.
- Maintaining documentation consistency.
- Following the approved architecture.
- Assisting with implementation.
- Reviewing repository structure.
- Identifying architectural inconsistencies.
- Maintaining engineering quality.
- Supporting phase transitions.
- Preparing engineering deliverables.

The AI must not introduce architectural changes without explicit approval from the Project Owner.

---

## 5. Standard Engineering Workflow

Every engineering task should follow the same workflow.

```text
User Request
        │
        ▼
Review Documentation
        │
        ▼
Review Current Phase
        │
        ▼
Review Architecture
        │
        ▼
Plan Implementation
        │
        ▼
Implement
        │
        ▼
Review Changes
        │
        ▼
Update Documentation
        │
        ▼
Prepare Commit
```

Documentation review must always precede implementation.

Implementation must always precede documentation updates.

---

## 6. Phase Lifecycle

Every development phase follows a standardized engineering lifecycle.

```text
Phase Planning
        │
        ▼
Implementation
        │
        ▼
Testing
        │
        ▼
Documentation Review
        │
        ▼
Documentation Update
        │
        ▼
Repository Review
        │
        ▼
Phase Completion
        │
        ▼
Next Phase Initialization
```

Each phase should be considered complete only after all required engineering activities have been successfully finished.

---

## 7. Repository Startup Workflow

Whenever a new engineering session begins, the AI should establish the current project context before performing any implementation.

```text
Read CHAT_BOOTSTRAP.md
        │
        ▼
Read PROJECT_CONTEXT.md
        │
        ▼
Read ARCHITECTURE.md
        │
        ▼
Read SESSION_CONTEXT.md
        │
        ▼
Read ROADMAP.md
        │
        ▼
Read TODO.md
        │
        ▼
Read CHANGELOG.md
        │
        ▼
Read ENGINEERING_MEMORY_GUIDE.md
        │
        ▼
Read ENGINEERING_MEMORY.md
        ▼
Repository Ready
```

The AI should not begin implementation before understanding the current repository state.

---

## 8. Documentation Update Rules

Documentation updates shall follow these rules.

| Document | Update Condition |
|----------|------------------|
| SESSION_CONTEXT.md | Current phase changes |
| TODO.md | Engineering tasks change |
| CHANGELOG.md | Engineering milestone completed |
| ROADMAP.md | Roadmap changes |
| ARCHITECTURE.md | Architecture changes |
| PROJECT_CONTEXT.md | Engineering vision changes |
| CHAT_BOOTSTRAP.md | Workflow changes |
| ENGINEERING_MEMORY.md | New engineering knowledge |
| ADR | New architectural decisions |
| HISTORY | Phase completion |

Routine implementation must not require modifications to static documentation.

---

## 9. Repository Review Rules

Before implementation, the AI should review:

- Current project phase.
- Active engineering tasks.
- Repository structure.
- Architecture consistency.
- Existing ADRs.
- Documentation consistency.

Implementation should not proceed when unresolved architectural inconsistencies exist.

---

## 10. AI Decision Rules

The AI may independently:

- Improve implementation quality.
- Refactor internal code.
- Improve documentation wording.
- Improve readability.
- Improve maintainability.

The AI must request approval before:

- Changing architecture.
- Renaming modules.
- Changing repository structure.
- Modifying engineering workflow.
- Introducing breaking changes.

---

## 11. Phase Completion Workflow

When a development phase is completed, the AI should perform the following engineering workflow.

```text
Review Repository
        │
        ▼
Review Documentation
        │
        ▼
Update SESSION_CONTEXT
        │
        ▼
Update TODO
        │
        ▼
Update CHANGELOG
        │
        ▼
Generate HISTORY
        │
        ▼
Review ADR
        │
        ▼
Review ROADMAP
        │
        ▼
Review ARCHITECTURE
        │
        ▼
Review ENGINEERING_MEMORY
        │
        ▼
Update ENGINEERING_MEMORY
        │
        ▼
Prepare Git Commit
        │
        ▼
Initialize Next Phase
```

All required documentation should be reviewed before the next phase begins.

---

## 12. New Phase Initialization

Before beginning a new development phase, the AI should:

- Review ROADMAP.md.
- Review SESSION_CONTEXT.md.
- Review TODO.md.
- Verify previous phase completion.
- Prepare the engineering work plan.
- Confirm implementation priorities.

Implementation should begin only after the new phase has been fully prepared.

---

## 13. Git Workflow

Engineering work should follow the official repository workflow.

```text
Implementation
        │
        ▼
Review
        │
        ▼
Documentation Update
        │
        ▼
Commit
        │
        ▼
Tag (Optional)
```

Commit messages should represent completed engineering milestones.

---

## 14. Review Checklist

Before considering engineering work complete, verify:

- Architecture consistency.
- Repository consistency.
- Documentation consistency.
- Implementation quality.
- Backward compatibility.
- Engineering completeness.

---

## 15. Trigger Commands

The following user commands trigger predefined engineering workflows.

| User Command | AI Action |
|--------------|-----------|
| Start Phase | Initialize a new development phase. |
| Continue Development | Resume implementation using the current project state. |
| Review Repository | Review repository consistency. |
| Review Documentation | Review documentation consistency. |
| Update Documentation | Update required project documents. |
| Complete Phase | Execute the Phase Completion Workflow. |
| Prepare Release | Review repository, finalize documentation, prepare commit and release artifacts. |

---

## 16. Maintenance Policy

AI_WORKFLOW.md should be updated only when one or more of the following changes occur:

- Engineering workflow changes.
- Documentation workflow changes.
- Repository workflow changes.
- Phase lifecycle changes.
- AI responsibilities change.

Routine implementation must not require modifications to this document.

---

# Document Status

| Item | Value |
|------|-------|
| Version | 1.0 |
| Status | Active |
| Classification | AI Engineering Workflow |
| Maintained By | Project Owner |
| Source of Truth | Repository |
# RCBT Session Context

# 1. Project Information

| Item | Value |
|------|-------|
| Project | Ruijie Cloud Backup Toolkit (RCBT) |
| Repository Branch | `main` |
| Current Phase | Phase 7.0 — Discovery Finalization |
| Status | Active |
| Current Milestone | Discovery Engine |

---

# 2. Project Progress

## Completed Phases

- ✅ Phase 1 — Project Bootstrap
- ✅ Phase 2 — Workspace
- ✅ Phase 3 — HAR Import & Parser
- ✅ Phase 4 — Request Discovery
- ✅ Phase 5 — Authentication Strategy
- ✅ Phase 6 — API Runtime Foundation

---

# 3. Current Objective

Complete the reverse engineering process of Ruijie Cloud so that the Runtime Layer can operate entirely from structured Discovery Metadata instead of directly depending on HAR files.

The primary deliverable of Phase 7.0 is a complete Discovery Metadata foundation that will become the engineering knowledge source for the future Knowledge Engine.

---

# 4. Current Focus

Complete the Discovery Engine (Phase 7.0) by producing validated Discovery Metadata that serves as the engineering foundation for the future Knowledge Engine.

---

# 5. Task Tracker

The active engineering task is maintained exclusively in:

```text
docs/TODO.md
```

All engineering implementation, validation, and production progress must follow the first unchecked checklist item in `docs/TODO.md`.

---

# 6. Current Execution Pipeline

```text
incoming/
        │
        ▼
backup.py
        │
        ▼
Workspace
        │
        ▼
HAR Importer
        │
        ▼
HAR Parser
        │
        ▼
Discovery Engine
        │
        ▼
Runtime Layer
        │
        ▼
Backup Workflow
        │
        ▼
Report Layer
        │
        ▼
Export Layer
```

This execution pipeline reflects the current technical architecture of RCBT.

---

# 7. Runtime Rules

Runtime Rules

- HAR Importer imports HAR files into the Workspace.
- HAR Parser interprets HAR data only.
- Runtime Layer must never consume HAR files directly.
- Runtime executes exclusively from Discovery Metadata.

---

# 8. Latest Completed

## Phase 6 — API Runtime Foundation

### Summary

Phase 6 established the Runtime Foundation, including:

- Authentication Runtime
- Session Management
- Login Service
- Runtime Layer Foundation
- Workflow Foundation

### Details

See:

```text
docs/CHANGELOG.md
```

---

# 9. Current Repository Structure

Main Controller

```text
backup.py
```

Core Modules

```text
development/
```

Reverse Engineering

```text
tools/
```

Discovery Output

```text
analysis/
```

Documentation

```text
docs/
```

Workspace

```text
projects/
```

Input HAR

```text
incoming/
```

---

# 10. Current Decisions

- **ADR-001** — `backup.py` remains the Main Controller.
- **ADR-002** — All core application modules are located under `development/`.
- **ADR-003** — HAR Parser is responsible only for interpreting HAR data.
- **ADR-004** — Runtime Layer must never depend directly on HAR files.
- **ADR-005** — All reverse engineering activities are performed using dedicated tools.
- **ADR-006** — The Knowledge Engine will be implemented after Phase 7.0 — Discovery Finalization.

---

# 11. Known Issues

Current engineering challenges

- HAR does not contain Session Cookies.
- HAR does not contain Authorization Headers.
- Authentication must be reverse engineered through the SSO workflow.
- Some endpoints still require additional investigation.

These limitations are being addressed during Phase 7.0.

---

# 12. Current Deliverables

Target outputs for Phase 7.0

- API Catalog
- Authentication Metadata
- Endpoint Catalog
- Workflow Catalog
- Storage Route Discovery
- Render Route Discovery
- Export Route Discovery
- Download Route Discovery
- Response Schema Discovery

Discovery outputs are stored under:

```text
analysis/
```

These artifacts will become the engineering foundation of the future Knowledge Engine.

---

# 13. Next Milestone

## Phase 7.1 — Knowledge Engine

### Objective

Build the Knowledge Layer that becomes the primary engineering knowledge source consumed by the Runtime Layer.

### Expected Output

```text
development/knowledge/
```

---

# 14. Documentation Status

Core Documents

- CHAT_BOOTSTRAP.md
- PROJECT_CONTEXT.md
- ARCHITECTURE.md
- SESSION_CONTEXT.md
- ROADMAP.md
- CHANGELOG.md
- TODO.md

Supporting Documentation

```text
docs/HISTORY/
docs/DECISIONS/
docs/TROUBLESHOOTING/
```

---

# 15. Current Engineering Principles

Engineering Principles

- Follow the approved project roadmap.
- Architectural changes require ADRs.
- Commits represent completed engineering milestones.
- Every implementation must be production-ready.
- Discovery Metadata is the engineering foundation for the future Knowledge Engine.
- Runtime Layer consumes Discovery Metadata rather than raw HAR files.

---

# 16. Current Status Summary

| Item | Value |
|------|-------|
| Current Phase | Phase 7.0 — Discovery Finalization |
| Current Milestone | Discovery Engine |
| Project Status | Active Development |
| Task Tracker | `docs/TODO.md` |
| Next Milestone | Phase 7.1 — Knowledge Engine |
| Repository Status | Active Development |
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

Complete the reverse engineering process of Ruijie Cloud so that the entire Runtime Layer can be built from structured Discovery metadata instead of directly depending on HAR files.

The primary output of Phase 7.0 is a complete Discovery Metadata foundation that will serve as the knowledge source for the future Knowledge Engine.

---

# 4. Current Focus

## Discovery Finalization

Primary focus

- Authentication Discovery
- RSA Discovery
- Cookie Discovery
- Redirect Discovery
- Session Validation
- Endpoint Discovery
- Workflow Discovery
- Storage Discovery
- Render Discovery
- Export Discovery
- Download Discovery
- Response Schema Discovery

---

# 5. Current Task

| Item | Value |
|------|-------|
| Task | Authentication Discovery |
| Status | In Progress |

Checklist

- [ ] RSA Endpoint Discovery
- [ ] Login Page Discovery
- [ ] Login Flow Validation
- [ ] Session Cookie Discovery
- [ ] Redirect Flow Discovery
- [ ] Session Validation Endpoint
- [ ] Authentication Metadata

---

# 6. Next Tasks

After Authentication Discovery is completed

1. Endpoint Discovery
2. Workflow Discovery
3. Storage Discovery
4. Render Discovery
5. Export Discovery
6. Download Discovery
7. Response Schema Discovery

---


# 7. Current Architecture

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

# 8. Runtime Architecture

```text
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

HAR Importer is responsible for importing HAR files into the Workspace.

HAR Parser is responsible only for interpreting HAR data.

Runtime Layer must never consume HAR files directly.

---

# 9. Latest Completed

Phase 6 successfully established the Runtime foundation.

Completed Modules

- Workspace
- HAR Importer
- Request Reader
- Endpoint Normalizer
- Credential Management
- SessionProvider
- LoginService
- AuthClient Foundation
- RenderClient
- Workflow Foundation
- API Runtime Foundation

---

# 10. Current Repository Structure

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

# 11. Current Decisions

### ADR-001
backup.py remains the Main Controller.

### ADR-002
All core application modules are located under the `development/` directory.

### ADR-003
HAR Parser is responsible only for interpreting HAR data.

### ADR-004
Runtime Layer must never depend directly on HAR files.

### ADR-005
All reverse engineering activities are performed using dedicated tools.

### ADR-006
The Knowledge Engine will be implemented after Discovery Finalization is complete.

---

# 12. Known Issues

Current engineering challenges

- Ruijie HAR does not contain Session Cookies.
- Ruijie HAR does not contain Authorization Headers.
- Authentication must be reverse engineered through the SSO workflow.
- Some endpoints still require additional investigation.

These limitations are being addressed during Discovery Finalization.

---

# 13. Current Deliverables

Target Phase 7.0

- Authentication Metadata
- Endpoint Catalog
- Workflow Catalog
- Storage Route Discovery
- Render Route Discovery
- Export Route Discovery
- Download Route Discovery
- Response Schema Discovery

All Discovery outputs are stored under

```text
analysis/
```

These outputs will become the engineering foundation for the future Knowledge Engine.

---

# 14. Next Milestone

Phase 7.1 — Knowledge Engine

Target

Build the Knowledge Layer that becomes the primary engineering knowledge source consumed by the Runtime Layer.

Expected Output

```text
development/knowledge/
```

---

# 15. Documentation Status

Core Documents

- CHAT_BOOTSTRAP.md
- PROJECT_CONTEXT.md
- ARCHITECTURE.md
- SESSION_CONTEXT.md
- ROADMAP.md
- CHANGELOG.md
- TODO.md

Supporting Documentation

History

```text
docs/HISTORY/
```

Architecture Decisions

```text
docs/DECISIONS/
```

Troubleshooting

```text
docs/TROUBLESHOOTING/
```

---

# 16. Engineering Notes

Current engineering principles

- Development follows the official project roadmap.
- Architectural changes require documented engineering decisions (ADR).
- Commits represent completed engineering milestones.
- Every implementation must be production-ready.
- Discovery Metadata becomes the engineering foundation for the future Knowledge Engine.
- Runtime Layer must consume structured Discovery outputs instead of raw HAR files whenever practical.

---

# 17. Current Status Summary

| Item | Value |
|------|-------|
| Current Phase | Phase 7.0 — Discovery Finalization |
| Current Goal | Complete Ruijie Cloud reverse engineering |
| Current Focus | Authentication Discovery |
| Next Milestone | Phase 7.1 — Knowledge Engine |
| Project Status | Active Development |
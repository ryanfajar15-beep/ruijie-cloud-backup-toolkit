# RCBT Roadmap

This roadmap defines the long-term engineering direction of the Ruijie Cloud Backup Toolkit (RCBT).

Each phase represents a major engineering milestone. New phases should be added only after the current phase has been successfully completed.

---

# Phase 1 — Project Bootstrap

Status

✅ Completed

Objective

Establish the initial project foundation.

Deliverables

- Repository Structure
- Development Environment
- Documentation Foundation
- Initial Project Configuration

---

# Phase 2 — Workspace

Status

✅ Completed

Objective

Build the Workspace infrastructure responsible for project lifecycle management.

Deliverables

- Workspace Initialization
- Project Lifecycle Management
- HAR Input Management
- Project Directory Structure

---

# Phase 3 — HAR Import & Parser

Status

✅ Completed

Objective

Import HAR files into the Workspace and transform captured traffic into structured requests.

Deliverables

- HAR Importer
- HAR Parser
- Request Reader
- Parsed Request Model

---

# Phase 4 — Request Discovery

Status

✅ Completed

Objective

Analyze parsed requests and establish the Discovery foundation.

Deliverables

- Request Classification
- Endpoint Discovery
- Request Catalog
- Initial Discovery Metadata

---

# Phase 5 — Authentication Strategy

Status

✅ Completed

Objective

Design the authentication architecture required for Runtime execution.

Deliverables

- Authentication Architecture
- Login Workflow
- Session Strategy
- Authentication Design

---

# Phase 6 — API Runtime Foundation

Status

✅ Completed

Objective

Build the Runtime foundation required to execute discovered application behavior.

Deliverables

- Authentication Runtime
- Session Provider
- Login Service
- Auth Client
- Credential Management
- Endpoint Configuration Foundation
- Runtime Layer Foundation
- Workflow Foundation

---

# Phase 7 — Discovery Engine

Status

🚧 In Progress

Objective

Complete the reverse engineering process so that the Runtime Layer no longer depends directly on HAR files.

---

## Phase 7.0 — Discovery Finalization

Status

🚧 In Progress

Objective

Complete all Discovery components.

Target

- Authentication Discovery
- RSA Discovery
- Cookie Discovery
- Redirect Discovery
- Session Validation Discovery
- Endpoint Discovery
- Workflow Discovery
- Storage Discovery
- Render Discovery
- Export Discovery
- Download Discovery
- Response Schema Discovery

Output

```text
analysis/
```

---

## Phase 7.1 — Knowledge Engine

Status

Planned

Objective

Build the Knowledge Layer as the primary engineering knowledge source consumed by the Runtime Layer.

Output

```text
development/knowledge/
```

---

## Phase 7.2 — Runtime Integration

Status

Planned

Objective

Integrate the Runtime Layer with the Knowledge Engine.

Output

- Integrated Runtime Layer
- Knowledge-driven Execution
- Runtime Validation

---

## Phase 7.3 — Production Optimization

Status

Planned

Objective

Prepare the toolkit for production deployment.

Target

- Runtime Hardening
- Performance Optimization
- Comprehensive Testing
- Documentation Finalization
- Production Readiness

---

# Future Phases

Future phases will be defined after successful completion of Phase 7 based on engineering priorities, architectural evolution, and project requirements.

---

# Roadmap Maintenance Policy

This roadmap should be updated only when one or more of the following changes occur:

- A new phase is introduced.
- A phase is completed.
- Engineering priorities change.
- Major architectural milestones are added.
- Project direction changes.

Routine implementation work must not require modifications to this document.

---

# Document Status

| Item | Value |
|------|-------|
| Version | 3.0 |
| Status | Active |
| Classification | Engineering Roadmap |
| Maintained By | Project Owner |
| Source of Truth | Repository |
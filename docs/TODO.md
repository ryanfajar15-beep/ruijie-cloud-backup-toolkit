# RCBT Engineering TODO

This document tracks active engineering tasks for the current development phase.

Completed work should be removed from this document and recorded in CHANGELOG.md.

---

# Current Phase

Phase 7.0 — Discovery Engine
============================

Current Objective
-----------------
Complete the Discovery Engine so that the Runtime Layer no longer depends directly on HAR files.


Current Task
------------
Stage 1 — API Catalog Discovery
-------------------------------

[x] Wrapper Endpoint Discovery
[x] API Endpoint Extraction
[x] API Catalog Normalization
[x] Module Discovery

[x] Method Discovery
[x] Request Count Analysis
[x] Request Parameter Discovery
[x] Response Type Discovery
[x] API Classification

[x] Generate api_catalog.json


Stage 2 — Authentication Metadata
---------------------------------

[ ] Login Page Metadata
[ ] RSA Metadata
[ ] Hidden Fields Metadata
[ ] Password Validation Metadata
[ ] Login Request Metadata
[ ] Session Cookie Metadata
[ ] Session Validation Metadata
[ ] Redirect Flow Metadata

[ ] Generate authentication_catalog.json


Stage 3 — Workflow Discovery
----------------------------

[ ] Project Workflow
[ ] Survey Workflow
[ ] Render Workflow
[ ] Export Workflow
[ ] Download Workflow

[ ] Generate workflow_catalog.json


Stage 4 — Response Discovery
----------------------------

[ ] Response Schema Discovery
[ ] Response Object Discovery
[ ] Error Response Discovery
[ ] Response Relationship Discovery

[ ] Generate response_catalog.json


Stage 5 — Knowledge Assembly
-----------------------------

[ ] API Catalog Validation
[ ] Authentication Catalog Validation
[ ] Workflow Catalog Validation
[ ] Response Catalog Validation

[ ] Cross Reference Validation
[ ] Knowledge Consistency Validation

[ ] Generate knowledge_index.json


Stage 6 — Production Discovery Engine
-------------------------------------

[ ] API Discovery Engine
[ ] Authentication Discovery Engine
[ ] Workflow Discovery Engine
[ ] Response Discovery Engine
[ ] Knowledge Engine Integration

[ ] Unit Test
[ ] Integration Test
[ ] Documentation



---

# Next Phase Preview

Phase 7.1 — Knowledge Engine

Planned Tasks

- [ ] Create Knowledge Layer
- [ ] Build Metadata Repository
- [ ] Implement Knowledge Loader
- [ ] Implement Runtime Knowledge Provider
- [ ] Validate Runtime integration

---

# TODO Maintenance Policy

This document contains only active engineering tasks.

Completed tasks should:

1. Be removed from this document.
2. Be recorded in CHANGELOG.md.
3. Be reflected in SESSION_CONTEXT.md when they affect the current project status.

Historical milestones must not remain in this document.

---

# Document Status

| Item | Value |
|------|-------|
| Version | 3.0 |
| Status | Active |
| Classification | Engineering Task Tracker |
| Maintained By | Project Owner |
| Source of Truth | Repository |
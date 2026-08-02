# RCBT Engineering TODO

This document tracks active engineering tasks for the current development phase.

Engineering progress must always follow the approved Discovery lifecycle.

Reverse Engineering
    ↓
Validation
    ↓
Discovery Metadata
    ↓
Production Discovery Engine
    ↓
Runtime Integration
    ↓
Production Validation

Completed work should be removed from this document and recorded in CHANGELOG.md.

---

# Current Phase

Phase 7.0 — Discovery Finalization
============================

Status

Active

---

# Current Objective

Build a validated Discovery Engine capable of producing production-ready metadata without Runtime directly depending on HAR files.

---

# Current Task

Stage 1 — API Discovery
=======================

Reverse Engineering
-------------------

[√] Discover Wrapper Endpoint
[√] Discover API Endpoint
[√] Discover API Module
[√] Discover API Method
[√] Discover Request Count
[√] Discover Request Parameters
[√] Discover Response Type
[√] Discover API Classification

Validation
----------

[ ] Validate Wrapper Endpoint
[ ] Validate API Endpoint
[ ] Validate API Module
[ ] Validate API Method
[ ] Validate Request Count
[ ] Validate Request Parameters
[ ] Validate Response Type
[ ] Validate API Classification

Discovery Metadata
------------------

[ ] Generate wrapper_endpoints.json
[ ] Generate module_catalog.json
[ ] Generate api_catalog.json

Production Discovery Engine
---------------------------

[ ] API Discovery Module
[ ] API Metadata Provider
[ ] Runtime API Integration

Production Validation
---------------------

[ ] API Discovery Test
[ ] API Metadata Validation

---

Stage 2 — Authentication Discovery
==================================

Reverse Engineering
-------------------

[√] Discover Login Page
[√] Discover RSA Endpoint
[√] Discover RSA Payload
[√] Discover Hidden Fields
[√] Discover Password Validation
[√] Discover Login Request
[√] Discover Domain
[√] Discover Session Cookie
[√] Discover Session Validation
[√] Discover Redirect Flow

Validation
----------

[ ] Validate Login Metadata
[ ] Validate RSA Metadata
[ ] Validate Hidden Fields Metadata
[ ] Validate Password Validation Metadata
[ ] Validate Login Request Metadata
[ ] Validate Domain Metadata
[ ] Validate Session Cookie Metadata
[ ] Validate Session Validation Metadata
[ ] Validate Redirect Metadata

Discovery Metadata
------------------

[ ] Generate login_metadata.json
[ ] Generate rsa_metadata.json
[ ] Generate hidden_fields_metadata.json
[ ] Generate password_validation_metadata.json
[ ] Generate login_request_metadata.json
[ ] Generate domain_catalog.json
[ ] Generate session_cookie_metadata.json
[ ] Generate session_validation_metadata.json
[ ] Generate redirect_flow_metadata.json
[ ] Generate authentication_catalog.json

Production Discovery Engine
---------------------------

[ ] Authentication Discovery Module
[ ] Authentication Metadata Provider
[ ] Runtime Authentication Integration

Production Validation
---------------------

[ ] Authentication Discovery Test
[ ] Authentication Metadata Validation

Stage 3 — Workflow Discovery
============================

Reverse Engineering
-------------------

[√] Discover Project Workflow
[√] Discover Survey Workflow
[√] Discover Render Workflow
[√] Discover Export Workflow
[ ] Discover Export API
[ ] Discover Download Workflow
[ ] Discover Download Artifact
[ ] Discover Download Domain

Validation
----------

[ ] Validate Project Workflow
[ ] Validate Survey Workflow
[ ] Validate Render Workflow
[ ] Validate Export Workflow
[ ] Validate Export API
[ ] Validate Download Workflow
[ ] Validate Download Artifact
[ ] Validate Download Domain

Discovery Metadata
------------------

[ ] Generate project_workflow_metadata.json
[ ] Generate survey_workflow_metadata.json
[ ] Generate render_workflow_metadata.json
[ ] Generate export_task_metadata.json
[ ] Generate download_artifact_metadata.json
[ ] Generate download_domain_metadata.json
[ ] Generate workflow_catalog.json

Production Discovery Engine
---------------------------

[ ] Workflow Discovery Module
[ ] Workflow Metadata Provider
[ ] Runtime Workflow Integration

Production Validation
---------------------

[ ] Workflow Discovery Test
[ ] Workflow Metadata Validation

---

Stage 4 — Response Discovery
============================

Reverse Engineering
-------------------

[ ] Discover Response Schema
[ ] Discover Response Object
[ ] Discover Response Relationship
[ ] Discover Error Response
[ ] Discover Success Response
[ ] Discover Response Mapping

Validation
----------

[ ] Validate Response Schema
[ ] Validate Response Object
[ ] Validate Response Relationship
[ ] Validate Error Response
[ ] Validate Success Response
[ ] Validate Response Mapping

Discovery Metadata
------------------

[ ] Generate response_schema_metadata.json
[ ] Generate response_object_metadata.json
[ ] Generate response_relationship_metadata.json
[ ] Generate error_response_metadata.json
[ ] Generate response_catalog.json

Production Discovery Engine
---------------------------

[ ] Response Discovery Module
[ ] Response Metadata Provider
[ ] Runtime Response Integration

Production Validation
---------------------

[ ] Response Discovery Test
[ ] Response Metadata Validation

Stage 5 — Knowledge Assembly
============================

Validation
----------

[ ] Validate API Catalog
[ ] Validate Authentication Catalog
[ ] Validate Workflow Catalog
[ ] Validate Response Catalog

Knowledge Assembly
------------------

[ ] Cross Reference API
[ ] Cross Reference Authentication
[ ] Cross Reference Workflow
[ ] Cross Reference Response

[ ] Validate Knowledge Consistency
[ ] Validate Metadata Integrity
[ ] Validate Metadata Relationship

Knowledge Metadata
------------------

[ ] Generate knowledge_index.json
[ ] Generate knowledge_catalog.json

Production Integration
----------------------

[ ] Knowledge Provider
[ ] Knowledge Loader
[ ] Runtime Knowledge Integration

Production Validation
---------------------

[ ] Knowledge Engine Test
[ ] Knowledge Integration Test


Knowledge Assembly prepares validated Discovery Metadata for Phase 7.1 (Knowledge Engine).

It does not implement the Knowledge Engine itself.

---

Stage 6 — Production Discovery Engine
=====================================

Production Discovery Engine
---------------------------

[ ] API Discovery Engine
[ ] Authentication Discovery Engine
[ ] Workflow Discovery Engine
[ ] Response Discovery Engine
[ ] Knowledge Discovery Engine

Runtime Integration
-------------------

[ ] Workspace Integration
[ ] Parser Integration
[ ] Discovery Engine Integration
[ ] Runtime Layer Integration
[ ] Backup Workflow Integration
[ ] Report Layer Integration

Production Validation
---------------------

[ ] Unit Test
[ ] Integration Test
[ ] End-to-End Test
[ ] Performance Validation
[ ] Documentation Review
[ ] Production Readiness Review

---

# Next Phase Preview

Phase 7.1 — Knowledge Engine
============================

Planned Tasks
-------------

[ ] Create Knowledge Layer
[ ] Build Metadata Repository
[ ] Implement Knowledge Loader
[ ] Implement Knowledge Provider
[ ] Implement Runtime Knowledge Service
[ ] Validate Runtime Knowledge Integration

---

# TODO Maintenance Policy

This document contains only active engineering tasks.

Engineering progress must follow the Discovery lifecycle:

Reverse Engineering
    ↓
Validation
    ↓
Discovery Metadata
    ↓
Production Discovery Engine
    ↓
Runtime Integration
    ↓
Production Validation

Rules
-----

1. Reverse Engineering (`tools/`) is Engineering Laboratory only.
2. Reverse Engineering success is not Production completion.
3. Discovery Metadata must be generated from validated findings.
4. Production implementation exists only under `development/`.
5. TODO checklists may only be marked PASS after Production implementation is complete.
6. Completed work must be removed from this document.
7. Completed milestones must be recorded in CHANGELOG.md.
8. SESSION_CONTEXT.md must reflect current engineering status.

---

# Document Status

| Item | Value |
|------|-------|
| Version | 4.0 |
| Status | Active |
| Classification | Engineering Task Tracker |
| Maintained By | Project Owner |
| Source of Truth | Repository |
| Discovery Lifecycle | Reverse Engineering → Validation → Discovery Metadata → Production Discovery Engine → Runtime Integration → Production Validation |
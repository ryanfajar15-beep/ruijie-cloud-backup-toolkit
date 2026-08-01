# RCBT Engineering TODO

This document tracks active engineering tasks for the current development phase.

Completed work should be removed from this document and recorded in CHANGELOG.md.

---

# Current Phase

Phase 7.0 — Discovery Finalization

Status

Active

---

# Current Objective

Complete the Discovery Engine so that the Runtime Layer no longer depends directly on HAR files.

---

# Authentication Discovery

- [ ] Discover RSA endpoint
- [ ] Analyze RSA request payload
- [ ] Identify login page workflow
- [ ] Identify login request sequence
- [ ] Discover session cookie generation
- [ ] Discover redirect workflow
- [ ] Discover session validation endpoint
- [ ] Generate Authentication Metadata

---

# Endpoint Discovery

- [ ] Discover API endpoints
- [ ] Classify endpoint categories
- [ ] Detect endpoint relationships
- [ ] Generate Endpoint Catalog

---

# Workflow Discovery

- [ ] Discover application workflows
- [ ] Identify request dependencies
- [ ] Build workflow relationships
- [ ] Generate Workflow Metadata

---

# Storage Discovery

- [ ] Discover storage endpoints
- [ ] Identify storage resources
- [ ] Document storage workflow

---

# Render Discovery

- [ ] Discover render endpoints
- [ ] Document rendering workflow

---

# Export Discovery

- [ ] Discover export endpoints
- [ ] Document export workflow

---

# Download Discovery

- [ ] Discover download endpoints
- [ ] Document download workflow

---

# Response Schema Discovery

- [ ] Analyze response structures
- [ ] Generate response schema catalog
- [ ] Identify reusable models

---

# Discovery Metadata

- [ ] Validate Authentication Metadata
- [ ] Validate Endpoint Metadata
- [ ] Validate Workflow Metadata
- [ ] Validate Response Metadata
- [ ] Validate Discovery consistency

---

# Phase 7 Exit Criteria

- [ ] Authentication Discovery completed
- [ ] Endpoint Discovery completed
- [ ] Workflow Discovery completed
- [ ] Storage Discovery completed
- [ ] Render Discovery completed
- [ ] Export Discovery completed
- [ ] Download Discovery completed
- [ ] Response Schema Discovery completed
- [ ] Discovery Metadata validated
- [ ] Runtime Layer can execute without directly parsing HAR

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
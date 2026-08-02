# RCBT Engineering Memory

> This document preserves long-term engineering knowledge that must not
> be lost throughout the lifetime of the Ruijie Cloud Backup Toolkit (RCBT).
>
> This document shall be maintained according to
> ENGINEERING_MEMORY_GUIDE.md.

---

# 1. Purpose

ENGINEERING_MEMORY.md stores engineering knowledge that cannot be
represented by TODO.md, CHANGELOG.md, SESSION_CONTEXT.md,
or other project documents.

It exists to preserve important engineering knowledge across
development phases, AI conversations, and engineering teams.

---

# 2. Engineering Agreements

---

## EM-0001

Date

2026-08-02

Title

Reverse Engineering and Production Development Separation

Context

Reverse engineering tools are required for investigation and laboratory
activities only.

Decision

The `tools/` directory shall only be used for reverse engineering,
analysis, validation, automation utilities, and engineering experiments.

Production implementation shall never execute directly from tools.

Impact

- Reverse engineering remains isolated.
- Production modules remain stable.
- Discovery output must be validated before implementation.

Status

Active

---

## EM-0002

Date

2026-08-02

Title

Discovery Validation Pipeline

Context

Discovery results cannot immediately become production code.

Decision

Every Discovery Stage shall follow this lifecycle:

Reverse Engineering

↓

Validation

↓

Discovery Metadata

↓

Production Discovery

↓

Production Validation

Impact

Runtime must never depend directly on reverse engineering results.

Status

Active

---

## EM-0003

Date

2026-08-02

Title

Repository Modification Workflow

Context

Manual editing frequently introduces inconsistencies.

Decision

Whenever repository modification is required, AI shall provide:

- Create File command
- Complete file content
- Run command
- Validation command

Manual editing should be avoided whenever possible.

Status

Active

---

## EM-0004

Date

2026-08-02

Title

Git Commit Policy

Decision

Git Commit shall only be performed after an entire Stage or Phase has
been completed.

Partial implementation must remain uncommitted unless explicitly
requested by the Project Owner.

Status

Active

---

# 3. Engineering Decisions

---

## ED-0001

Date

2026-08-02

Title

Workflow Discovery Must Be Evidence Driven

Decision

Discovery metadata shall only be generated from validated HAR evidence.

Reason

Runtime must never rely on assumptions.

Impact

Every workflow requires reverse engineering evidence before becoming
Discovery Metadata.

Status

Active

---

## ED-0002

Date

2026-08-02

Title

Successful HAR Is Mandatory For Download Workflow

Decision

Download Workflow discovery requires successful HAR capture.

Failed HAR may be used for comparison only.

Reason

Failed exports do not contain complete download workflow.

Status

Active

---

# 4. Investigation Results

---

## IR-0001

HAR comparison successfully identifies:

- workflow differences
- endpoint differences
- export differences

Successful HAR provides the primary evidence for Workflow Discovery.

Status

Verified

---

# 5. Reverse Engineering Findings

---

## RF-0001

Current reverse engineering process relies on:

- HAR Parser
- Workflow Comparison
- Export Chain Trace

These outputs require validation before becoming Discovery Metadata.

Status

Active

---

# 6. Lessons Learned

---

## LL-0001

Do not classify CDN assets as Download Artifacts.

---

## LL-0002

Do not implement Runtime directly from reverse engineering outputs.

---

# 7. Known Pitfalls

---

## KP-0001

HAR Sanitized may remove:

- Cookies
- Authorization
- Sensitive headers

Additional validation may be required.

---

# 8. AI Working Agreements

---

## AI-0001

Whenever a new repository file is required, AI shall provide:

- mkdir (if required)
- touch command
- Complete file content

AI shall not request manual file creation.

---

## AI-0002

Large repository files shall be delivered as:

Part 1/x

Part 2/x

Part 3/x

without requiring manual merging.

---

# 9. Rejected Decisions

---

## RD-0001

Rejected

Generating Runtime directly from reverse engineering output.

Reason

Violates Discovery architecture.

---

# 10. Pending Investigations

---

## PI-0001

Finalize Download Workflow Discovery.

Status

In Progress

---

## PI-0002

Generate workflow_catalog.json after Workflow Discovery validation.

Status

Pending

---

# 11. Maintenance Policy

This document stores engineering knowledge only.

Routine implementation progress belongs to:

- TODO.md
- SESSION_CONTEXT.md
- CHANGELOG.md

---

# Document Status

| Item | Value |
|------|-------|
| Version | 1.0 |
| Status | Active |
| Classification | Engineering Knowledge |
| Maintained By | Project Owner & AI Engineering Partner |
| Source of Truth | Repository |
# RCBT Engineering Memory Guide

> This document defines the purpose, scope, ownership, review process,
> update policy, and maintenance rules for ENGINEERING_MEMORY.md.
>
> ENGINEERING_MEMORY.md preserves engineering knowledge that must not
> be lost throughout the lifetime of the project.
>
> Unlike TODO.md, CHANGELOG.md, SESSION_CONTEXT.md, or ROADMAP.md,
> ENGINEERING_MEMORY.md stores long-term engineering knowledge rather
> than project status or implementation progress.
>
> This document is the official Source of Truth for maintaining
> ENGINEERING_MEMORY.md.

---

# 1. Purpose

ENGINEERING_MEMORY.md exists to preserve engineering knowledge that
cannot be represented by other project documents.

Its objective is to ensure that important engineering decisions,
agreements, investigations, lessons learned, and technical findings
remain available throughout the lifetime of the project.

The document reduces repeated investigation, prevents recurring mistakes,
and enables AI or future engineers to continue development without
losing engineering context.

---

# 2. Scope

ENGINEERING_MEMORY.md stores engineering knowledge.

It complements existing project documentation.

It does NOT replace:

- CHAT_BOOTSTRAP.md
- AI_WORKFLOW.md
- SESSION_CONTEXT.md
- TODO.md
- CHANGELOG.md
- ROADMAP.md
- PROJECT_CONTEXT.md
- ARCHITECTURE.md

---

# 3. Ownership

ENGINEERING_MEMORY.md is jointly maintained by:

- Project Owner
- AI Engineering Partner

Responsibilities

Project Owner

- Validate long-term engineering knowledge.
- Approve important engineering decisions.
- Ensure engineering consistency.

AI Engineering Partner

- Detect new engineering knowledge.
- Recommend new memory entries.
- Keep the document concise.
- Prevent duplicate knowledge.

---

# 4. Responsibilities

ENGINEERING_MEMORY.md preserves knowledge such as:

- Engineering Agreements
- Engineering Decisions
- Investigation Results
- Reverse Engineering Findings
- Lessons Learned
- Known Pitfalls
- AI Working Agreements
- Rejected Decisions
- Pending Investigations
- Chat Transfer Knowledge

---

# 5. Information That MUST NOT Be Stored

The following information belongs elsewhere.

| Information | Document |
|------------|----------|
| Current Phase | SESSION_CONTEXT.md |
| Current Task | SESSION_CONTEXT.md |
| Active Checklist | TODO.md |
| Completed Milestones | CHANGELOG.md |
| Future Planning | ROADMAP.md |
| Technical Architecture | ARCHITECTURE.md |
| Project Identity | PROJECT_CONTEXT.md |
| AI Workflow | AI_WORKFLOW.md |

ENGINEERING_MEMORY.md should never duplicate those documents.

---

# 6. Review Trigger

The AI Engineering Partner must review
ENGINEERING_MEMORY.md whenever one of the following occurs:

- Starting a new Phase.
- Completing a Stage.
- Completing a Phase.
- Finishing an investigation.
- Making an engineering decision.
- Establishing a new engineering agreement.
- Preparing documentation before Git Commit.

If no new engineering knowledge is identified,
no update is required.

---

# 7. Update Triggers

ENGINEERING_MEMORY.md MUST be updated whenever one or more of the
following conditions occur.

## 7.1 Engineering Agreement

Examples

- Commit only after Stage or Phase completion.
- AI must provide complete files.
- AI must provide Create File commands.

---

## 7.2 Engineering Decision

Example

Decision

Reverse Engineering and Production Discovery are separated.

Reason

Runtime must never depend on unvalidated reverse engineering.

Impact

Discovery workflow becomes:

Reverse Engineering

↓

Validation

↓

Discovery Metadata

↓

Production Discovery

---

## 7.3 Investigation Result

Example

Successful HAR contains Download Workflow.

Failed HAR does not.

Decision

Workflow Discovery must always validate using successful HAR.

---

## 7.4 Reverse Engineering Finding

Example

Export workflow identified through HAR comparison.

---

## 7.5 Lesson Learned

Example

CDN assets must never be classified as Download Artifacts.

---

## 7.6 Known Pitfall

Example

HAR Sanitized removes cookies and authorization data.

---

## 7.7 AI Working Agreement

Example

Never request manual editing if the AI can provide a complete file.

---

## 7.8 Rejected Decision

Example

Rejected

Generate Runtime directly from HAR.

Reason

Violates Discovery architecture.

---

## 7.9 Pending Investigation

Example

Download endpoint still requires validation using successful HAR.

---

# 8. Update Workflow

Engineering Work

↓

Review ENGINEERING_MEMORY.md

↓

Did new engineering knowledge appear?

↓

NO

↓

Continue Engineering

↓

YES

↓

Update ENGINEERING_MEMORY.md

↓

Continue Engineering

---

# 9. Entry Template

Each memory entry should follow this format.

--------------------------------------------------

Date

Category

Title

Context

Decision

Reason

Impact

Related Phase

Related Files

Status

--------------------------------------------------

Only include information that provides long-term engineering value.

---

# 10. Engineering Principle

A piece of information belongs in ENGINEERING_MEMORY.md only if the
following statement is true:

"If this knowledge is lost, future engineers or AI will likely repeat
the same investigation, repeat the same mistake, or make a worse
engineering decision."

If YES

Store it.

If NO

Do not store it.

---

# 11. Relationship with Other Documents

| Document | Responsibility |
|----------|----------------|
| CHAT_BOOTSTRAP.md | AI Working Rules |
| AI_WORKFLOW.md | Engineering Workflow |
| SESSION_CONTEXT.md | Current Project Status |
| TODO.md | Active Engineering Tasks |
| CHANGELOG.md | Completed Milestones |
| ROADMAP.md | Long-Term Planning |
| ARCHITECTURE.md | Technical Architecture |
| ENGINEERING_MEMORY.md | Long-Term Engineering Knowledge |

ENGINEERING_MEMORY.md complements the documentation ecosystem.

It should never duplicate information already maintained elsewhere.

---

# 12. When NOT to Update

ENGINEERING_MEMORY.md should NOT be updated for:

- Routine implementation.
- Code refactoring.
- Bug fixes without new engineering knowledge.
- Documentation wording improvements.
- Checklist updates.
- Progress updates.
- Phase status changes.
- Git commits.
- Repository restructuring that does not introduce new engineering knowledge.

These changes belong to their respective project documents.

---

# 13. Phase Completion Review

Before declaring a Stage or Phase complete, verify:

- [ ] ENGINEERING_MEMORY.md reviewed.
- [ ] New engineering knowledge identified.
- [ ] Memory updated if required.
- [ ] Duplicate entries removed.
- [ ] Existing entries remain valid.

If no new engineering knowledge exists,
ENGINEERING_MEMORY.md should remain unchanged.

---
# 14. Maintenance Policy

ENGINEERING_MEMORY.md should remain concise.

Do NOT store:

- Daily progress
- Temporary notes
- Raw logs
- HAR output
- Large reverse engineering data
- Runtime output

Instead, summarize engineering knowledge.

---

# Document Status

| Item | Value |
|------|-------|
| Version | 1.0 |
| Status | FREZZE |
| Classification | Engineering Knowledge Guide |
| Maintained By | Project Owner & AI Engineering Partner |
| Source of Truth | Repository |
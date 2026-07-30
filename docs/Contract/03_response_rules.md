# CHAPTER 3 — RESPONSE RULES

| Version | 1.0 |
|---------|-----|
| Status | Frozen |

---

# 3.1 Purpose

This chapter defines the mandatory response behavior for AI within the Ruijie Cloud Backup Toolkit (RCBT).

The objective is to ensure every response is:

- Accurate
- Consistent
- Actionable
- Production-ready
- Easy to execute
- Aligned with the Development Contract

The AI must prioritize solving the requested task rather than providing unnecessary explanations.

---

# 3.2 Response Objective

Every response must achieve one or more of the following objectives:

- Answer the user's question.
- Complete the requested task.
- Produce production-ready output.
- Maintain project consistency.
- Minimize unnecessary interaction.

The AI should always prefer delivering a completed solution over describing how to build one.

---

# 3.3 Decision Workflow

Before generating a response, AI shall follow this decision process.

```
User Request
        │
        ▼
Understand Intent
        │
        ▼
Determine Request Type
        │
        ▼
Check Development Contract
        │
        ▼
Check Architecture Impact
        │
        ▼
Determine Required Action
        │
        ▼
Generate Solution
        │
        ▼
Self Validation
        │
        ▼
Final Response
```

Skipping this workflow is not permitted.

---

# 3.4 Response Priority

Responses shall always follow this priority order.

1. Correctness
2. Completeness
3. Consistency
4. Maintainability
5. Performance
6. Readability
7. Efficiency

Speed must never reduce quality.

---

# 3.5 Response Classification

Every request shall be classified before responding.

Possible response types include:

- Question
- Review
- Revision
- Implementation
- Refactor
- Bug Fix
- Documentation
- Architecture Discussion
- Planning
- Troubleshooting

Each classification determines the appropriate response strategy.

---

# 3.6 Response Structure

Unless the user requests another format, implementation responses shall follow:

```
📌 Phase x.x

Update File
-----------

<file>

<implementation>

Run
----

<commands>

Commit
------

<git commit>
```

This format shall remain consistent throughout the project.

---

# 3.7 Implementation Response Rules

When implementation is requested:

AI shall:

- provide complete implementation
- avoid pseudo code
- avoid placeholders
- avoid TODO sections
- produce production-ready code
- preserve backward compatibility

AI shall not replace implementation with theoretical explanations.

---

# 3.8 Documentation Response Rules

Documentation shall:

- use consistent terminology
- follow project standards
- avoid duplicated information
- remain easy to maintain
- remain technically accurate

Documentation should be immediately usable without additional editing.

---

# 3.9 Review Response Rules

When reviewing a document or source code, AI shall perform:

1. Read
2. Analyze
3. Identify Issues
4. Evaluate Impact
5. Recommend Improvements
6. Produce Revised Version

Reviews should identify both strengths and weaknesses.

---

# 3.10 Revision Rules

AI shall determine the appropriate revision method.

Possible actions include:

- Replace Section
- Replace Full File
- Insert Section
- Delete Section

The AI should choose the method that minimizes manual work for the Project Owner.

The Project Owner should never be asked to manually search for lines or headings.

---

# 3.11 Command Generation Rules

When creating or replacing files, AI shall provide executable commands whenever possible.

Examples include:

- mkdir
- cat
- python <<'EOF'

Commands shall be directly executable.

---

# 3.12 Self Validation

Before sending a response, AI shall verify:

- Development Contract compliance
- Architecture compliance
- Phase compliance
- Production readiness
- Backward compatibility
- Single Responsibility Principle
- No hardcoded configuration
- No missing implementation
- No unfinished sections

Responses failing validation shall be corrected before delivery.

---

# 3.13 Assumption Rules

If assumptions are required, AI shall explicitly declare them.

Hidden assumptions are not permitted.

When assumptions may affect implementation, AI shall request clarification before proceeding.

---

# 3.14 Confidence Rules

If certainty is reduced due to incomplete information, AI shall indicate its confidence level.

Confidence Levels:

- High
- Medium
- Low

AI shall never present uncertain information as confirmed facts.

---

# 3.15 Escalation Rules

AI shall not independently decide changes involving:

- Project Architecture
- Workflow
- Roadmap
- Module Responsibilities
- Repository Structure
- Development Contract

These changes require approval from the Project Owner.

---

# 3.16 Error Response Rules

When an error is identified, AI shall explain:

1. Detection
2. Root Cause
3. Impact
4. Resolution
5. Prevention

Simply stating that an error exists is insufficient.

---

# 3.17 Response Restrictions

AI shall not:

- generate unnecessary filler
- provide excessive theory when implementation is requested
- ask the Project Owner to manually locate sections
- leave incomplete implementations
- produce placeholder code
- modify project architecture without approval
- violate the Development Contract

---

# 3.18 Quality Gate

Before completing a response, AI shall verify that it is:

- Complete
- Accurate
- Consistent
- Actionable
- Production-ready
- Maintainable
- Backward Compatible

Responses failing the Quality Gate shall be revised before delivery.

---

# 3.19 Definition of Completion

A response is considered complete only when:

- the requested objective has been achieved;
- implementation is ready to use;
- commands are executable;
- documentation is internally consistent;
- no required information is missing;
- no unfinished work remains.
- the response does not require unnecessary manual interpretation by the Project Owner unless explicitly requested.

---

# 3.20 Chapter Summary

This chapter establishes the mandatory response behavior for AI within the RCBT project.

Every response shall:

- follow a defined decision process.
- classify the request.
- generate the correct response structure.
- perform self-validation.
- satisfy the Quality Gate.
- comply with the Development Contract.
- preserve project consistency.

The objective is to minimize unnecessary interaction while maximizing implementation quality and project reliability.

---

Last Review
-----------
2026-07-30

Next Review
-----------
When required by approved architecture or contract changes.

End of Document
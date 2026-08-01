# Engineering Decision Record

Decision ID
-----------
0001

Title
-----
API Catalog Discovery becomes the foundation of Phase 7 Discovery.

Status
------
Accepted

Date
----
2026-08-02

Related Documents
-----------------
- ROADMAP.md
- TODO.md
- SESSION_CONTEXT.md
- ARCHITECTURE.md

Context
-------
Phase 7.0 is responsible for building the Discovery Engine.

Originally, Authentication Discovery was scheduled as the first implementation task.

During reverse engineering, it was confirmed that Ruijie Cloud exposes almost all internal APIs through a generic wrapper endpoint.

Example:

POST /webproxy/common/api

The actual API information is transported inside the request payload.

Example payload:

{
    "api": "/plan/render/async/start",
    "module": "survey",
    "method": "POST",
    "querys": {},
    "params": {}
}

Therefore Authentication Discovery cannot be implemented independently.

A complete inventory of internal APIs must exist before endpoint classification, authentication mapping, workflow reconstruction, and runtime implementation.

Decision
--------
Introduce API Catalog Discovery as the first execution stage of Phase 7.

The Discovery process will follow this order:

1. API Catalog Discovery
2. Authentication Discovery
3. Endpoint Discovery
4. Workflow Discovery
5. Response Discovery
6. Production Discovery Engine

Architecture Impact
-------------------
None.

Repository Impact
-----------------
None.

Runtime Impact
--------------
None.

Documentation Impact
--------------------
TODO.md will be reordered.

SESSION_CONTEXT.md current task will be updated.

ROADMAP.md remains unchanged because project milestones do not change.

Benefits
--------
- Eliminates duplicate endpoint discovery.
- Creates a single source of truth for internal APIs.
- Makes Authentication Discovery deterministic.
- Simplifies Workflow Discovery.
- Reduces implementation complexity.
- Improves maintainability.

Consequences
------------
Only the execution order changes.

Project scope remains unchanged.

Backward Compatibility
----------------------
Fully backward compatible.

Approval
--------
Accepted for Phase 7 Discovery implementation.
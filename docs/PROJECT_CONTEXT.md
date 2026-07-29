# PROJECT_CONTEXT.md

> **Single Source of Truth (SSOT)**
>
> This document defines the complete engineering context for the Ruijie Cloud Backup Toolkit (RCBT).
>
> It serves as the authoritative reference for architecture, implementation, workflow, engineering standards, development philosophy, and future roadmap.
>
> Every implementation, documentation update, refactoring, and architectural decision must remain consistent with this document unless superseded by an approved Architecture Decision Record (ADR).

---

# 1. Document Information

| Item | Value |
|------|-------|
| Document | PROJECT_CONTEXT.md |
| Project | Ruijie Cloud Backup Toolkit (RCBT) |
| Document Type | Engineering Context Document |
| Status | Active |
| Version | 1.0 |
| Repository | ruijie-cloud-backup-toolkit |
| Language | English |
| Audience | Project Owner, Software Engineers, Future Contributors, AI Assistants |
| Priority | Highest |

---

# 2. Purpose

PROJECT_CONTEXT.md is the highest-level engineering document of the project.

Unlike README, ROADMAP, CHANGELOG, or TODO documents, this document captures the complete engineering knowledge required to understand, continue, maintain, and extend the project without depending on historical conversations.

The objectives of this document are:

- Preserve architectural consistency.
- Preserve engineering decisions.
- Preserve implementation philosophy.
- Eliminate ambiguity.
- Reduce onboarding time.
- Define project boundaries.
- Prevent architecture drift.
- Ensure future development follows the established design.

Whenever implementation conflicts with this document, the conflict must be resolved before coding continues.

---

# 3. Project Overview

Ruijie Cloud Backup Toolkit (RCBT) is a modular Python application designed to reverse engineer, analyze, backup, restore, and document Ruijie Cloud resources through structured API discovery.

The project starts from a HAR (HTTP Archive) file exported from Ruijie Cloud.

Rather than functioning as a simple backup script, RCBT is designed as an engineering platform capable of understanding Ruijie Cloud communication and converting captured browser sessions into reproducible backup artifacts.

The toolkit is intended to support:

- HAR analysis
- API discovery
- Authentication discovery
- API catalog generation
- Cloud resource backup
- Configuration restore
- Report generation
- Future automation

The project emphasizes long-term maintainability over rapid implementation.

---

# 4. Vision

Create a production-grade toolkit capable of completely understanding Ruijie Cloud communication while providing reliable backup and restore capabilities through a clean, modular, and maintainable architecture.

RCBT is intended to become an engineering platform rather than a collection of independent scripts.

---

# 5. Engineering Philosophy

The project follows several engineering principles.

## 5.1 Architecture First

Architecture always has higher priority than implementation speed.

Temporary solutions that compromise long-term maintainability should be avoided.

---

## 5.2 Modular Design

Every module must solve exactly one problem.

Responsibilities should never overlap.

Business logic should never be duplicated.

---

## 5.3 Separation of Concerns

Filesystem,
HAR parsing,
authentication discovery,
API discovery,
backup,
restore,
report generation,

must remain independent.

Each module communicates only through well-defined outputs.

---

## 5.4 Reusability

Every module should be reusable by future components.

Modules must avoid unnecessary dependencies.

---

## 5.5 Incremental Development

The project is developed through small, testable phases.

Each completed phase becomes the stable foundation for the next phase.

---

## 5.6 Documentation Driven Development

Documentation is considered part of the implementation.

Architecture decisions must be documented before significant implementation changes.

---

## 5.7 Git Driven Development

Every significant milestone should be preserved through Git commits.

Major project milestones should be marked using Git tags.

---

# 6. Project Goals

The primary goals are:

- Analyze HAR files.
- Discover HTTP API endpoints.
- Extract authentication information.
- Build an API catalog.
- Download Ruijie Cloud resources.
- Backup project configurations.
- Restore backed-up configurations.
- Generate structured reports.
- Support multiple independent projects.
- Maintain production-grade engineering quality.

---

# 7. Non-Goals

The project intentionally avoids:

- Monolithic architecture.
- Hardcoded project-specific logic.
- Tight coupling between modules.
- Direct filesystem manipulation by parser modules.
- Temporary prototype implementations.
- Manual project organization.
- Features outside the documented roadmap.

---

# 8. Current Project Status

| Item | Value |
|------|-------|
| Status | Active Development |
| Current Version | v0.4.0-dev |
| Current Sprint | Sprint 2 |
| Current Phase | Phase 3.5.5 |
| Current Focus | Main Controller Refactoring |
| Current Entry Point | backup.py |
| Repository | GitHub |
| Documentation | Active |
| Workspace System | Designed |
| Parser | Versioned |

---

# 9. Current Development Position

## Completed

- Git repository initialized.
- GitHub repository connected.
- Documentation structure established.
- HAR parser implemented.
- Request discovery completed.
- Request catalog generation completed.
- Authentication discovery prototype completed.
- Workspace architecture designed.
- Project directory structure finalized.

---

## In Progress

- Refactor backup.py into the Main Controller.
- Integrate Workspace Manager.
- Transition from parser-oriented execution to workspace-oriented execution.

---

## Next Milestone

Workspace-driven project lifecycle.

---

# 10. High-Level System Architecture

The system follows a sequential execution pipeline.

```text
Incoming HAR
      │
      ▼
Workspace Manager
      │
      ▼
Project Initialization
      │
      ▼
HAR Parser
      │
      ▼
Request Discovery
      │
      ▼
Authentication Discovery
      │
      ▼
API Discovery
      │
      ▼
Backup Engine
      │
      ▼
Report Generator
      │
      ▼
Restore Engine
```

Each stage produces structured artifacts consumed by the next stage.

No module should bypass previous stages.

No module should directly manipulate downstream components.

---

# 11. Core Design Principles

The entire project follows these engineering principles:

- Single Responsibility Principle (SRP)
- Clean Architecture
- Dependency Direction
- Explicit Data Flow
- Modular Design
- Logging First
- Reusable Components
- Versioned Development
- Incremental Delivery
- Git-Driven Development
- Documentation-Driven Development
- Maintainability First
- Production-Oriented Design

---

# End of Part 1
---

# 12. Architecture Decision Records (ADR)

This section records the major architectural decisions that define the project.

Only final and accepted decisions are documented here.

Any future architectural modification that changes one of these decisions must update this section before implementation.

---

## ADR-001 — Main Controller

**Status**

Accepted

**Decision**

`backup.py` is the single entry point of the application.

Every execution starts from `backup.py`.

No other module may act as the application entry point.

**Reason**

A single entry point simplifies:

- execution flow
- dependency management
- logging
- configuration loading
- future CLI implementation

It also prevents duplicated startup logic.

**Impact**

- All modules become callable components.
- The application has one predictable execution flow.
- Future CLI implementation becomes straightforward.

---

## ADR-002 — Workspace Owns Filesystem

**Status**

Accepted

**Decision**

Only the Workspace subsystem may create, rename, move, or organize project directories.

No parser, discovery, backup, or exporter module may directly manipulate the filesystem structure.

**Reason**

Filesystem management is an infrastructure concern.

Business modules should remain independent from directory structures.

Separating these responsibilities improves maintainability and testability.

**Impact**

- Parser becomes reusable.
- Backup engine remains independent.
- Export modules remain independent.
- Workspace becomes the infrastructure layer.

---

## ADR-003 — Parser Must Remain Pure

**Status**

Accepted

**Decision**

Parser modules are responsible only for reading and interpreting HAR files.

Parser modules must never:

- create folders
- move files
- generate project structures
- perform backup operations

**Reason**

The parser should remain reusable by future modules and testing tools.

Keeping the parser pure minimizes dependencies and simplifies testing.

**Impact**

- Parser can be reused independently.
- Workspace handles infrastructure.
- Business logic remains isolated.

---

## ADR-004 — Incoming Directory

**Status**

Accepted

**Decision**

Every HAR file must first be placed inside the `incoming/` directory.

Example:

```text
incoming/
    padang_padang.har
```

The application automatically detects HAR files located in this directory.

**Reason**

The user should only need to provide a HAR file.

Manual project creation is unnecessary.

This design minimizes operational complexity.

**Impact**

User workflow becomes:

1. Export HAR.
2. Copy HAR into `incoming/`.
3. Run `python3 backup.py`.

Nothing else is required.

---

## ADR-005 — Automatic Workspace Creation

**Status**

Accepted

**Decision**

For every HAR file discovered inside `incoming/`, the application automatically creates a project workspace.

Example:

```text
projects/
└── 20260729_padang_padang/
```

The original HAR file is moved into the project workspace.

**Reason**

Each backup should become an isolated project.

Keeping every execution independent simplifies future restore operations and reporting.

**Impact**

Multiple backups can coexist safely.

Each workspace becomes self-contained.

---

## ADR-006 — Standard Project Structure

**Status**

Accepted

**Decision**

Every project workspace must follow the same directory layout.

```text
projects/
└── <project_name>/
    ├── project.json
    ├── input/
    │   └── session.har
    ├── output/
    ├── report/
    └── logs/
```

**Reason**

A predictable structure simplifies:

- automation
- debugging
- backup
- restore
- report generation

Future modules can rely on stable paths.

---

## ADR-007 — Project Metadata

**Status**

Accepted

**Decision**

Each project contains a `project.json` file describing project metadata.

Typical information includes:

- project id
- project name
- creation timestamp
- source HAR
- application version
- execution status

**Reason**

Project metadata should be separated from implementation artifacts.

This enables future indexing, searching, and project management.

---

## ADR-008 — Development Source Layout

**Status**

Accepted

**Decision**

Source code remains inside the `development/` directory during current development.

Example:

```text
development/
    parser/
    workspace/
    exporter/
```

**Reason**

Renaming the entire source tree during active development introduces unnecessary work.

The current layout is stable and already integrated with the existing codebase.

Refactoring directory names provides little architectural benefit.

---

## ADR-009 — Versioned Parser

**Status**

Accepted

**Decision**

Parser implementations are versioned.

Example:

```text
development/parser/versions/

parser_v01.py
parser_v02.py
parser_v03.py
parser_v04.py
```

**Reason**

Parser evolution should remain traceable.

Previous implementations become valuable references during debugging and regression testing.

---

## ADR-010 — Documentation Driven Development

**Status**

Accepted

**Decision**

Major architectural decisions must be documented before implementation.

Engineering documentation is considered part of the software.

**Reason**

The project is expected to evolve over a long period.

Documentation reduces ambiguity and allows future contributors to understand the reasoning behind architectural choices.

---

# End of Part 2
---

# 13. System Architecture

## 13.1 Architectural Overview

RCBT follows a layered modular architecture.

Each layer has a clearly defined responsibility and communicates only through explicit interfaces.

The application is designed to minimize coupling while maximizing component reusability.

```text
                +----------------------+
                |      backup.py       |
                |   Main Controller    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Workspace Manager   |
                +----------+-----------+
                           |
        +------------------+------------------+
        |                                     |
        v                                     v
+-------------------+               +-------------------+
|   Project Manager |               |   HAR Importer    |
+-------------------+               +-------------------+
        |                                     |
        +------------------+------------------+
                           |
                           v
                +----------------------+
                |     HAR Parser       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Request Discovery    |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Authentication       |
                | Discovery            |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | API Discovery        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Backup Engine        |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Report Generator     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Export Engine        |
                +----------------------+
```

---

## 13.2 Architectural Layers

The application is divided into several logical layers.

### Application Layer

Responsible for:

- startup
- execution flow
- orchestration

Current component:

- `backup.py`

---

### Workspace Layer

Responsible for:

- project creation
- filesystem management
- path resolution
- project metadata

Current components:

- workspace.py
- project_info.py
- path_manager.py
- har_importer.py

---

### Parsing Layer

Responsible for reading HAR files.

Current components:

- parser_v01
- parser_v02
- parser_v03
- parser_v04

---

### Discovery Layer

Responsible for transforming parsed requests into structured knowledge.

Includes:

- Request Discovery
- Authentication Discovery
- API Discovery

---

### Backup Layer

Responsible for downloading resources from Ruijie Cloud.

Produces backup artifacts.

---

### Reporting Layer

Responsible for generating reports and exports.

Supported outputs may include:

- JSON
- HTML
- CSV
- Excel

---

## 13.3 Dependency Rules

Dependencies must always point downward.

```text
backup.py
      │
      ▼
Workspace
      │
      ▼
Parser
      │
      ▼
Discovery
      │
      ▼
Backup
      │
      ▼
Report
```

Reverse dependencies are prohibited.

Example:

Parser must never call Workspace.

Discovery must never call Main Controller.

Backup must never create project folders.

---

## 13.4 Communication Principles

Each module communicates only through explicit data.

Modules must not access another module's internal state.

Communication should occur through:

- return values
- models
- configuration objects

Global state should be avoided whenever possible.

---

## 13.5 Design Constraints

The following constraints define the architecture.

### One Entry Point

The application starts only from:

```text
backup.py
```

---

### One Workspace

Every execution belongs to exactly one project workspace.

---

### One Source HAR

Each workspace originates from one HAR session.

---

### Predictable Execution

Every run follows the same processing sequence.

No module may skip mandatory stages.

---

### Reusable Components

Every business module should be reusable outside the main application.

Whenever possible, modules should avoid assumptions about filesystem layout or execution environment.

---

# End of Part 3
---

# 14. Workspace System

## 14.1 Purpose

The Workspace System is responsible for managing the lifecycle of every backup project.

Its primary objective is to transform an incoming HAR file into a fully structured and isolated project workspace that can be processed independently by the remaining application modules.

The Workspace subsystem is the only component responsible for project organization and filesystem management.

---

## 14.2 Responsibilities

The Workspace subsystem is responsible for:

- Detecting incoming HAR files.
- Creating new project workspaces.
- Generating standard directory structures.
- Moving HAR files into project input directories.
- Creating project metadata.
- Managing project paths.
- Providing workspace information to downstream modules.

The Workspace subsystem must not perform:

- HAR parsing
- API discovery
- Authentication extraction
- Backup operations
- Report generation

---

## 14.3 Workspace Lifecycle

Every execution follows the same lifecycle.

```text
User exports HAR
        │
        ▼
Copy HAR into incoming/
        │
        ▼
Run backup.py
        │
        ▼
Workspace detects HAR
        │
        ▼
Create Project
        │
        ▼
Move HAR
        │
        ▼
Generate project.json
        │
        ▼
Return Workspace Context
        │
        ▼
Continue Processing
```

No additional manual preparation should be required.

---

## 14.4 Incoming Directory

The `incoming/` directory is the entry point of every project.

Example:

```text
incoming/
├── padang_padang.har
├── ubud_dream.har
└── pandawa_hills.har
```

Users only need to copy HAR files into this directory.

The application automatically processes every valid HAR file found inside.

---

## 14.5 Automatic Project Creation

For every HAR file discovered inside `incoming/`, a new workspace is automatically created.

Example:

```text
projects/
└── 20260729_padang_padang/
```

The workspace identifier should uniquely identify each execution.

Typical naming strategy:

```text
YYYYMMDD_project_name
```

Example:

```text
20260729_padang_padang
20260729_ubud_dream
20260730_pandawa_hills
```

The naming strategy may evolve in future versions, but project uniqueness must always be preserved.

---

## 14.6 Standard Workspace Structure

Every workspace follows the same directory layout.

```text
projects/
└── <project_name>/
    ├── project.json
    ├── input/
    │   └── session.har
    │
    ├── output/
    │
    ├── report/
    │
    └── logs/
```

This structure must remain consistent across all projects.

Future modules rely on these predefined locations.

---

## 14.7 Project Metadata

Every workspace contains a `project.json` file.

Its purpose is to describe the workspace independently of its generated artifacts.

Typical metadata includes:

- Project ID
- Project Name
- Source HAR filename
- Creation timestamp
- Application version
- Processing status
- Current phase
- Execution history (future)

This file becomes the authoritative metadata source for the workspace.

---

## 14.8 Workspace Context

Once a workspace has been created, the Workspace subsystem returns a Workspace Context object.

The context provides downstream modules with standardized project information.

Typical information includes:

- Project Root
- Input Directory
- Output Directory
- Report Directory
- Log Directory
- HAR File Location
- Project Metadata

Downstream modules should rely on this context rather than constructing filesystem paths manually.

---

## 14.9 Filesystem Ownership

Workspace exclusively owns the project filesystem.

Only Workspace may:

- Create directories
- Move HAR files
- Resolve paths
- Generate project metadata

Other modules must treat the workspace as read-only infrastructure.

Parser modules, discovery modules, and backup modules must never create project directories.

---

## 14.10 Future Expansion

The Workspace System has been intentionally designed for future enhancements.

Possible future capabilities include:

- Multiple workspace management
- Workspace indexing
- Project search
- Execution history
- Resume interrupted backups
- Workspace cleanup
- Parallel execution support

These capabilities should be implemented without changing the core workspace lifecycle.

---

## 14.11 Design Principles

The Workspace System follows the following principles:

- Automatic over manual.
- Convention over configuration.
- Predictable directory layout.
- Isolated project execution.
- Single filesystem owner.
- Stable project metadata.
- Future scalability.

---

# End of Part 4
---

# 15. Processing Workflow & Data Flow

## 15.1 Purpose

The Processing Workflow defines the complete execution sequence of the application.

Its purpose is to ensure every backup execution follows a predictable, repeatable, and deterministic process.

Each stage produces artifacts that become the input for the next stage.

Modules must never skip stages or bypass the established processing pipeline.

---

## 15.2 High-Level Workflow

The complete execution flow is illustrated below.

```text
User
 │
 ▼
Export HAR
 │
 ▼
incoming/
 │
 ▼
backup.py
 │
 ▼
Workspace Manager
 │
 ▼
Project Workspace
 │
 ▼
HAR Parser
 │
 ▼
Request Discovery
 │
 ▼
Authentication Discovery
 │
 ▼
API Discovery
 │
 ▼
Backup Engine
 │
 ▼
Report Generator
 │
 ▼
Exporter
 │
 ▼
Finished
```

Every execution follows this sequence.

---

## 15.3 Execution Stages

### Stage 1 — HAR Acquisition

Input:

```text
incoming/*.har
```

Output:

Workspace creation request.

Responsibilities:

- Detect HAR files.
- Validate file existence.
- Ignore unsupported files.

---

### Stage 2 — Workspace Initialization

Input:

HAR file.

Output:

Project Workspace.

Generated artifacts:

```text
project.json
input/session.har
```

Responsibilities:

- Create workspace.
- Generate metadata.
- Move HAR into input directory.
- Return Workspace Context.

---

### Stage 3 — HAR Parsing

Input:

```text
input/session.har
```

Output:

Parsed HTTP request collection.

Responsibilities:

- Read HAR.
- Validate HAR format.
- Parse requests.
- Preserve request ordering.

Parser must not perform business logic.

---

### Stage 4 — Request Discovery

Input:

Parsed requests.

Output:

```text
output/request_catalog.json
```

Responsibilities:

- Detect endpoints.
- Classify HTTP methods.
- Extract URLs.
- Extract headers.
- Extract query parameters.

---

### Stage 5 — Authentication Discovery

Input:

Parsed requests.

Output:

```text
output/auth_catalog.json
```

Responsibilities:

- Authorization tokens.
- Cookies.
- CSRF tokens.
- Session identifiers.
- Tenant information.
- User information.

---

### Stage 6 — API Discovery

Input:

Request Catalog

Authentication Catalog

Output:

```text
output/api_catalog.json
```

Responsibilities:

- Merge discovered endpoints.
- Remove duplicates.
- Classify APIs.
- Build endpoint relationships.

---

### Stage 7 — Backup Engine

Input:

API Catalog

Authentication Catalog

Workspace Context

Output:

Downloaded resources.

Responsibilities:

- Authenticate requests.
- Download resources.
- Preserve hierarchy.
- Handle pagination.
- Retry failed requests.

---

### Stage 8 — Report Generation

Input:

Execution results.

Output:

```text
report/
```

Responsibilities:

- Execution summary.
- Statistics.
- Errors.
- Download summary.

---

### Stage 9 — Export

Input:

Project artifacts.

Output examples:

```text
backup.zip
report.html
catalog.json
```

Supported export formats may include:

- JSON
- HTML
- CSV
- Excel
- ZIP

---

## 15.4 Data Flow

The following diagram illustrates artifact generation throughout the execution.

```text
HAR
 │
 ▼
Parsed Requests
 │
 ├──────────────┐
 ▼              ▼
Request      Authentication
Catalog      Catalog
 │              │
 └──────┬───────┘
        ▼
    API Catalog
        │
        ▼
 Backup Engine
        │
        ▼
 Backup Files
        │
        ▼
 Reports
        │
        ▼
 Export
```

Each artifact has a clearly defined producer and consumer.

---

## 15.5 Processing Contracts

Each module must satisfy the following contracts.

### Workspace

Produces:

Workspace Context

Consumes:

HAR file

---

### Parser

Produces:

Parsed Requests

Consumes:

Workspace Context

---

### Request Discovery

Produces:

Request Catalog

Consumes:

Parsed Requests

---

### Authentication Discovery

Produces:

Authentication Catalog

Consumes:

Parsed Requests

---

### API Discovery

Produces:

API Catalog

Consumes:

Request Catalog

Authentication Catalog

---

### Backup Engine

Produces:

Backup Files

Consumes:

Workspace Context

API Catalog

Authentication Catalog

---

### Report Generator

Produces:

Reports

Consumes:

Execution Results

---

### Export Engine

Produces:

Export Packages

Consumes:

Workspace Artifacts

---

## 15.6 Error Handling Strategy

Processing should stop immediately when a critical stage fails.

Critical failures include:

- Missing HAR file.
- Invalid HAR format.
- Workspace initialization failure.
- Parser failure.

Non-critical failures include:

- Single endpoint download failure.
- Retry exhaustion.
- Partial export failure.

Whenever possible, non-critical failures should be logged while allowing processing to continue.

---

## 15.7 Logging Strategy

Every stage should generate structured logs.

Typical information includes:

- Timestamp
- Processing stage
- Module name
- Severity
- Message
- Exception details (if applicable)

Logs should be written into:

```text
logs/backup.log
```

Future versions may support log rotation and multiple log levels.

---

## 15.8 Workflow Principles

The processing workflow follows these principles:

- Sequential execution.
- Deterministic outputs.
- Explicit artifact generation.
- Immutable intermediate artifacts.
- Reproducible execution.
- Failure isolation.
- Clear ownership of responsibilities.

---

# End of Part 5
---

# 16. Module Responsibilities

## 16.1 Purpose

This section defines the responsibility boundaries of every major module within the project.

Each module has one clearly defined purpose.

Responsibilities must never overlap.

Whenever new functionality is introduced, it should be assigned to an existing module only if it aligns with that module's responsibility.

Otherwise, a new module should be created.

---

# 16.2 Main Controller

Location

```text
backup.py
```

Purpose

Acts as the single application entry point.

Responsibilities

- Start application execution.
- Load configuration.
- Initialize logging.
- Initialize Workspace.
- Execute processing pipeline.
- Handle global exceptions.
- Display execution summary.

Must NOT

- Parse HAR.
- Discover APIs.
- Download resources.
- Generate reports.
- Manipulate business data.

---

# 16.3 Workspace Module

Location

```text
development/workspace/
```

Purpose

Manage project lifecycle and filesystem.

Responsibilities

- Detect incoming HAR files.
- Create project workspace.
- Generate project metadata.
- Move HAR files.
- Resolve project paths.
- Return Workspace Context.

Components

```text
workspace.py
project_info.py
path_manager.py
har_importer.py
```

Must NOT

- Parse HAR.
- Detect APIs.
- Download resources.

---

# 16.4 Parser Module

Location

```text
development/parser/
```

Purpose

Read and interpret HAR files.

Responsibilities

- Validate HAR.
- Read requests.
- Preserve request order.
- Normalize parsed data.
- Return parsed requests.

Components

```text
modules/
versions/
```

Must NOT

- Create folders.
- Move files.
- Perform API discovery.
- Download resources.

Output

```text
Parsed Requests
```

---

# 16.5 Request Discovery Module

Purpose

Extract request information from parsed HAR data.

Responsibilities

- Detect endpoints.
- Extract HTTP methods.
- Extract URLs.
- Extract query parameters.
- Extract request headers.

Produces

```text
request_catalog.json
```

Consumes

```text
Parsed Requests
```

---

# 16.6 Authentication Discovery Module

Purpose

Extract authentication-related information.

Responsibilities

- Authorization header.
- Cookies.
- CSRF tokens.
- Session identifiers.
- Tenant identifiers.
- User identifiers.

Produces

```text
auth_catalog.json
```

Consumes

```text
Parsed Requests
```

---

# 16.7 API Discovery Module

Purpose

Create a structured API catalog.

Responsibilities

- Merge endpoints.
- Remove duplicates.
- Detect endpoint relationships.
- Classify APIs.
- Build API metadata.

Produces

```text
api_catalog.json
```

Consumes

```text
Request Catalog
Authentication Catalog
```

---

# 16.8 Backup Engine

Purpose

Download Ruijie Cloud resources.

Responsibilities

- Authenticate requests.
- Execute API calls.
- Handle pagination.
- Handle retries.
- Preserve downloaded resources.

Produces

```text
backup/
```

Consumes

```text
Workspace Context
API Catalog
Authentication Catalog
```

---

# 16.9 Restore Engine

Purpose

Restore backed-up resources.

Responsibilities

- Load backup.
- Validate resources.
- Restore configuration.
- Execute restore operations.
- Generate restore summary.

Consumes

```text
backup/
```

---

# 16.10 Report Generator

Location

```text
development/report/
```

Purpose

Generate execution reports.

Responsibilities

- Execution summary.
- Statistics.
- Error reports.
- Processing duration.
- Download summary.

Produces

```text
report/
```

---

# 16.11 Export Module

Location

```text
development/exporter/
```

Purpose

Export project artifacts.

Responsibilities

- JSON export.
- HTML export.
- CSV export.
- Excel export.
- ZIP packaging.

Consumes

Project Artifacts.

Produces

Export Packages.

---

# 16.12 Shared Models

Future versions should introduce dedicated models shared between modules.

Examples

```text
WorkspaceContext

ParsedRequest

RequestCatalog

AuthenticationCatalog

ApiCatalog

BackupArtifact

ExecutionResult
```

Shared models reduce coupling between modules.

---

# 16.13 Dependency Rules

Allowed dependency direction

```text
backup.py
        │
        ▼
Workspace
        │
        ▼
Parser
        │
        ▼
Discovery
        │
        ▼
Backup
        │
        ▼
Report
        │
        ▼
Exporter
```

Reverse dependencies are prohibited.

Examples

Parser must never import Workspace.

Workspace must never import Backup Engine.

Exporter must never import Parser.

Report Generator must never import Backup Engine.

---

# 16.14 Responsibility Matrix

| Module | Owns Filesystem | Business Logic | Output |
|---------|-----------------|---------------|--------|
| Main Controller | ❌ | Execution | Pipeline |
| Workspace | ✅ | Project Lifecycle | Workspace Context |
| Parser | ❌ | HAR Parsing | Parsed Requests |
| Request Discovery | ❌ | Request Analysis | Request Catalog |
| Authentication Discovery | ❌ | Authentication Analysis | Authentication Catalog |
| API Discovery | ❌ | API Analysis | API Catalog |
| Backup Engine | ❌ | Resource Download | Backup Files |
| Restore Engine | ❌ | Restore Operations | Restore Results |
| Report Generator | ❌ | Reporting | Reports |
| Export Module | ❌ | Export | Export Packages |

---

# 16.15 Design Principles

Every module should satisfy the following rules.

- One responsibility.
- Explicit input.
- Explicit output.
- No hidden dependencies.
- No filesystem ownership except Workspace.
- No duplicated business logic.
- Easily testable.
- Easily replaceable.
- Future extensible.

---

# End of Part 6
---

# 17. Engineering Standards

## 17.1 Purpose

This section defines the engineering standards used throughout the project.

Every implementation must follow these standards to ensure consistency, maintainability, readability, and long-term scalability.

Coding style should never depend on personal preference.

---

# 17.2 General Principles

The project follows these engineering principles.

- Readability over cleverness.
- Explicit is better than implicit.
- Composition over duplication.
- Small functions.
- Small modules.
- Predictable behavior.
- Consistent naming.
- Production-quality code.

Every commit should improve or preserve code quality.

---

# 17.3 Python Version

Current target:

```text
Python 3.11+
```

Future code should remain compatible with the project's supported Python version.

---

# 17.4 Coding Style

The project follows:

- PEP 8
- PEP 257
- Type Hints
- Explicit Imports

Recommended formatter:

```text
black
```

Recommended linter:

```text
ruff
```

Recommended type checker:

```text
mypy
```

---

# 17.5 File Naming Convention

Python files use:

```text
snake_case.py
```

Examples

```text
workspace.py

project_info.py

auth_discovery.py

path_manager.py
```

Avoid

```text
Workspace.py

ProjectInfo.py

AuthDiscovery.py
```

---

# 17.6 Class Naming Convention

Classes use:

```text
PascalCase
```

Examples

```python
WorkspaceManager

ProjectInfo

HarImporter

ParserV04
```

---

# 17.7 Function Naming Convention

Functions use:

```text
snake_case
```

Examples

```python
create_workspace()

load_project()

parse_requests()

build_request_catalog()
```

---

# 17.8 Variable Naming

Variables use:

```text
snake_case
```

Examples

```python
project_root

request_list

workspace_context

auth_catalog
```

Avoid abbreviations unless they are universally understood.

Good

```python
request_catalog
```

Avoid

```python
req_cat
```

---

# 17.9 Constant Naming

Constants use:

```python
UPPER_CASE
```

Example

```python
DEFAULT_TIMEOUT

MAX_RETRY

PROJECT_VERSION
```

---

# 17.10 Package Organization

Each package owns one responsibility.

Example

```text
workspace/

parser/

backup/

restore/

report/

exporter/
```

Packages should not overlap responsibilities.

---

# 17.11 Function Design

Functions should be:

- Small.
- Predictable.
- Easy to test.

Preferred size:

```text
20–50 lines
```

Large functions should be decomposed into helper functions.

---

# 17.12 Method Responsibilities

Each method should perform one logical task.

Example

Good

```python
create_workspace()

move_har()

generate_metadata()
```

Avoid

```python
process_everything()
```

---

# 17.13 Error Handling

Errors should never be silently ignored.

Preferred

```python
try:
    ...
except Exception as exc:
    logger.exception(exc)
    raise
```

Avoid

```python
except:
    pass
```

---

# 17.14 Logging Standard

Logging should replace unnecessary print statements.

Use

```python
logger.info()

logger.warning()

logger.error()

logger.exception()
```

Avoid

```python
print()
```

except for CLI output.

---

# 17.15 Type Hints

Public functions should use type hints whenever practical.

Example

```python
def create_workspace(project_name: str) -> WorkspaceContext:
    ...
```

---

# 17.16 Documentation Standard

Every public class and function should include a docstring.

Example

```python
def parse_requests() -> list:
    """
    Parse HTTP requests from the HAR file.

    Returns:
        List of parsed requests.
    """
```

---

# 17.17 Comments

Comments should explain:

- Why.

Not

- What.

Good

```python
# Preserve request order because
# authentication tokens may depend
# on previous requests.
```

Avoid

```python
# Increment i

i += 1
```

---

# 17.18 Configuration

Avoid hardcoded values.

Configuration should be centralized whenever possible.

Examples

Good

```python
config.timeout
```

Avoid

```python
timeout = 30
```

inside business logic.

---

# 17.19 Dependency Management

Business modules should avoid unnecessary imports.

Dependencies should always point downward.

Example

```text
Workspace

↓

Parser

↓

Discovery

↓

Backup
```

Reverse dependencies are prohibited.

---

# 17.20 Testing Philosophy

Every module should be testable independently.

Testing should not require:

- Network access
- Manual interaction
- Existing project state

Modules should support isolated execution whenever possible.

---

# 17.21 Code Review Checklist

Before committing code, verify:

- Responsibility is correct.
- No duplicated logic.
- Naming follows convention.
- Type hints added.
- Logging implemented.
- Errors handled correctly.
- Functions remain small.
- Documentation updated if necessary.

---

# 17.22 Engineering Principles Summary

Every implementation should satisfy:

- Single Responsibility
- Maintainability
- Testability
- Readability
- Reusability
- Explicit Data Flow
- Minimal Coupling
- Consistent Naming
- Documentation First
- Production Quality

---

# End of Part 7
---

# 18. Development Workflow

## 18.1 Purpose

This section defines the official development workflow used throughout the project.

Every implementation should follow the same engineering process to ensure consistency, traceability, and maintainability.

Development is not limited to writing code.

Documentation, testing, version control, and architectural consistency are considered integral parts of the engineering process.

---

# 18.2 Development Lifecycle

Every feature follows the same lifecycle.

```text
Planning
    │
    ▼
Architecture Review
    │
    ▼
Implementation
    │
    ▼
Testing
    │
    ▼
Documentation Update
    │
    ▼
Git Commit
    │
    ▼
Git Push
    │
    ▼
Project Review
```

Skipping stages is discouraged.

---

# 18.3 Implementation Workflow

Every implementation should follow these steps.

Step 1

Review PROJECT_CONTEXT.md.

Step 2

Confirm the current phase.

Step 3

Review existing architecture.

Step 4

Implement one logical feature.

Step 5

Run local testing.

Step 6

Update documentation if necessary.

Step 7

Commit changes.

Step 8

Push changes to GitHub.

---

# 18.4 Git Workflow

Current strategy:

Single main branch.

```text
main
```

Development currently occurs directly on `main`.

Future versions may introduce:

```text
main

develop

feature/*
```

when the project complexity requires branch-based development.

---

# 18.5 Commit Convention

Commits should follow Conventional Commits.

Supported prefixes include:

```text
feat:
fix:
docs:
refactor:
test:
perf:
build:
chore:
style:
```

Examples

```text
feat(workspace): add project initialization

fix(parser): preserve request order

docs: update PROJECT_CONTEXT

refactor(backup): simplify execution pipeline
```

Commit messages should describe the intention rather than implementation details.

---

# 18.6 Git Tags

Major milestones should be tagged.

Examples

```text
v0.1.0

v0.2.0

v0.3.0

v0.4.0
```

Tags represent stable engineering checkpoints.

They should not be created for incomplete work.

---

# 18.7 Documentation Workflow

Documentation is considered part of the implementation.

Whenever architecture changes, documentation should be updated before continuing development.

Primary documents include:

```text
README.md

PROJECT_CONTEXT.md

ARCHITECTURE.md

ROADMAP.md

CHANGELOG.md

TODO.md
```

Each document has a specific responsibility.

---

## README.md

Purpose

User introduction.

Contains

- installation
- overview
- usage

---

## PROJECT_CONTEXT.md

Purpose

Engineering reference.

Contains

- architecture
- decisions
- workflow
- engineering standards

Highest priority document.

---

## ARCHITECTURE.md

Purpose

System overview.

Contains

- high-level architecture
- module overview

---

## ROADMAP.md

Purpose

Long-term planning.

Contains

- phases
- milestones
- future implementation

---

## CHANGELOG.md

Purpose

Engineering history.

Contains

- completed milestones
- version history

---

## TODO.md

Purpose

Current development state.

Contains

- current sprint
- current phase
- next tasks

---

# 18.8 Documentation Update Rules

Update documentation whenever:

- Architecture changes.
- New module introduced.
- New ADR accepted.
- Workflow changes.
- Major feature completed.

Minor bug fixes generally do not require documentation updates.

---

# 18.9 Versioning Strategy

The project follows incremental versioning.

Development builds

```text
v0.x.x-dev
```

Stable milestones

```text
v0.x.x
```

Future stable release

```text
v1.0.0
```

---

# 18.10 Release Workflow

Typical milestone workflow

```text
Feature Complete
        │
        ▼
Testing
        │
        ▼
Documentation Update
        │
        ▼
Git Commit
        │
        ▼
Git Push
        │
        ▼
Git Tag
```

Only stable milestones should receive Git tags.

---

# 18.11 Daily Development Workflow

Typical daily workflow.

```text
Pull Latest Code
        │
        ▼
Review PROJECT_CONTEXT
        │
        ▼
Implement Feature
        │
        ▼
Run Tests
        │
        ▼
Update Documentation
        │
        ▼
Commit
        │
        ▼
Push
```

---

# 18.12 AI Collaboration Workflow

AI is treated as an engineering assistant rather than an implementation authority.

AI should:

- Follow PROJECT_CONTEXT.md.
- Respect ADR decisions.
- Preserve module boundaries.
- Avoid introducing architectural changes without discussion.

AI should not:

- Redesign the project without approval.
- Change established workflows.
- Introduce undocumented architecture.

Whenever a significant architectural change is proposed, it should first be documented as a new ADR before implementation.

---

# 18.13 Engineering Rules

The following rules apply throughout the project.

- Architecture first.
- Documentation first.
- Code second.
- Test before commit.
- Commit before push.
- Push before release.
- Preserve Git history.
- Keep modules independent.
- Avoid unnecessary refactoring.
- Never sacrifice maintainability for speed.

---

# End of Part 8
---

# 19. Project Status & Roadmap

## 19.1 Purpose

This section records the current state of the project.

Unlike previous sections, the contents of this chapter are expected to evolve as development progresses.

This section provides a quick overview of:

- Current project status
- Active development phase
- Technical debt
- Known issues
- Future milestones
- Long-term roadmap

---

# 19.2 Current Status

| Item | Status |
|------|--------|
| Project | Active Development |
| Current Version | v0.4.0-dev |
| Current Sprint | Sprint 2 |
| Current Phase | Phase 3.5.5 |
| Repository | GitHub Connected |
| Workspace System | Designed |
| Documentation | Active |
| Backup Engine | Not Started |
| Restore Engine | Not Started |

---

# 19.3 Completed Milestones

The following milestones have been completed.

## Project Initialization

Status

Completed

Deliverables

- Git repository initialized
- GitHub repository connected
- Initial documentation created

---

## Parser Foundation

Status

Completed

Deliverables

- HAR validation
- HAR loading
- Request parsing
- Endpoint normalization
- Request catalog generation

---

## Authentication Discovery Prototype

Status

Completed

Deliverables

- Authentication discovery prototype
- Authorization detection
- Cookie discovery
- Authentication reporting

---

## Workspace Architecture

Status

Completed

Deliverables

- Workspace design
- Incoming directory workflow
- Project structure
- Workspace lifecycle
- Metadata strategy

---

# 19.4 Current Sprint

Sprint

Sprint 2

Primary Objective

Refactor the application around the Workspace architecture and transform `backup.py` into the Main Controller.

Current Tasks

- Refactor `backup.py`
- Integrate Workspace Manager
- Build execution pipeline
- Prepare Backup Engine integration

---

# 19.5 Upcoming Milestones

The next planned milestones are:

1. Main Controller
2. Workspace Integration
3. Backup Engine
4. Report Generator
5. Export Module
6. Restore Engine
7. Production CLI
8. Version 1.0 Release

---

# 19.6 Technical Debt

The following technical debt has been identified.

## Parser Versions

Multiple parser versions are intentionally retained for historical reference.

Future evaluation should determine whether older versions should remain archived or be consolidated.

---

## Temporary Development Structure

The `development/` directory remains the active source tree.

Future refactoring may reorganize packages after the project reaches a stable architecture.

---

## Missing Shared Models

Dedicated shared models have not yet been introduced.

Examples include:

- WorkspaceContext
- ParsedRequest
- ApiCatalog
- BackupArtifact

These models should be introduced before large-scale feature expansion.

---

## Configuration Management

Configuration is currently minimal.

A centralized configuration system should be introduced before production release.

---

# 19.7 Known Issues

Current known issues include:

- Backup Engine has not yet been implemented.
- Restore Engine has not yet been implemented.
- API relationship mapping is still limited.
- Authentication extraction requires additional validation against more HAR sessions.
- Multi-project execution has not yet been tested.

These issues are expected during the current development stage.

---

# 19.8 Future Roadmap

The long-term roadmap consists of the following major phases.

## Phase 4

Backup Engine

Objectives

- Resource download
- API execution
- Retry strategy
- Pagination handling

---

## Phase 5

Report Generation

Objectives

- Execution report
- HTML report
- Statistics
- Error reporting

---

## Phase 6

Export System

Objectives

- JSON export
- HTML export
- CSV export
- Excel export
- ZIP packaging

---

## Phase 7

Restore Engine

Objectives

- Restore resources
- Validate backup
- Recovery workflow

---

## Phase 8

Production Release

Objectives

- CLI stabilization
- Documentation completion
- Performance optimization
- Version 1.0 release

---

# 19.9 Success Criteria

The project will be considered production-ready when the following criteria are satisfied.

- Stable Workspace system
- Complete Backup Engine
- Functional Restore Engine
- Comprehensive API catalog
- Structured reporting
- Export capabilities
- Production documentation
- Automated testing
- Stable CLI

---

# 19.10 Long-Term Vision

Future versions may introduce:

- Incremental backup
- Differential backup
- Parallel download
- Cloud synchronization
- Scheduling
- Plugin architecture
- GUI application
- API server
- Docker deployment
- Multi-user support

These items are outside the scope of Version 1.0.

---

# End of Part 9
---
---

# 20. Engineering Guidelines

## 20.1 Purpose

This chapter defines the operational rules that every contributor must follow throughout the development lifecycle.

These guidelines ensure architectural consistency, maintainability, and long-term scalability.

Unless explicitly approved, these rules should not be violated.

---

# 20.2 Before Coding Checklist

Before starting any implementation, verify the following:

- [ ] Read the current PROJECT_CONTEXT.md.
- [ ] Confirm the current development phase.
- [ ] Confirm the current sprint objective.
- [ ] Review existing Architecture Decision Records (ADR).
- [ ] Verify module responsibility.
- [ ] Ensure the proposed implementation belongs to the correct module.
- [ ] Avoid duplicate functionality.
- [ ] Confirm implementation aligns with the current roadmap.

Coding should only begin after all items have been reviewed.

---

# 20.3 During Coding Checklist

While implementing new functionality:

- [ ] Follow Single Responsibility Principle.
- [ ] Keep functions small and predictable.
- [ ] Use descriptive naming.
- [ ] Avoid hardcoded values.
- [ ] Add logging where appropriate.
- [ ] Preserve module boundaries.
- [ ] Keep business logic independent from infrastructure.
- [ ] Avoid unnecessary dependencies.
- [ ] Write maintainable code.

---

# 20.4 Before Commit Checklist

Before creating a Git commit:

- [ ] Code executes successfully.
- [ ] No syntax errors.
- [ ] Imports are clean.
- [ ] Logging reviewed.
- [ ] Documentation updated (if required).
- [ ] No temporary debugging code remains.
- [ ] Commit message follows project convention.

---

# 20.5 Before Release Checklist

Before creating a release tag:

- [ ] All planned features completed.
- [ ] Documentation updated.
- [ ] ROADMAP reviewed.
- [ ] CHANGELOG updated.
- [ ] TODO reviewed.
- [ ] PROJECT_CONTEXT updated (if architecture changed).
- [ ] All major tests completed.
- [ ] Repository pushed to GitHub.

---

# 20.6 Engineering Rules

The following rules apply throughout the project.

## Rule 1

Architecture takes precedence over implementation speed.

---

## Rule 2

Documentation is part of the implementation.

---

## Rule 3

Parser modules remain pure.

Parser modules must never manipulate project directories.

---

## Rule 4

Workspace owns the filesystem.

No other module may create or organize project directories.

---

## Rule 5

Business modules remain independent.

Modules communicate only through defined interfaces and artifacts.

---

## Rule 6

One module, one responsibility.

If responsibilities begin to overlap, refactoring should be considered.

---

## Rule 7

Avoid unnecessary refactoring.

Stable architecture is preferred over continuous restructuring.

---

## Rule 8

Preserve Git history.

Meaningful commits are preferred over large undocumented changes.

---

## Rule 9

Every architectural change requires documentation.

Major architectural changes should update:

- PROJECT_CONTEXT.md
- ADR (if applicable)
- ARCHITECTURE.md (if applicable)

---

## Rule 10

Never sacrifice maintainability for short-term convenience.

---

# 20.7 Project Terminology

The following terminology is used consistently throughout the project.

| Term | Definition |
|------|------------|
| Workspace | An isolated project created from a HAR session. |
| Project | A single backup execution stored under `projects/`. |
| Incoming | Directory containing new HAR files awaiting processing. |
| Workspace Context | Standardized project information returned by the Workspace module. |
| Request Catalog | Structured collection of discovered HTTP requests. |
| Authentication Catalog | Structured authentication information extracted from requests. |
| API Catalog | Structured API database built from discovered endpoints. |
| Artifact | Any generated output consumed by another module. |
| ADR | Architecture Decision Record. |
| Pipeline | Ordered sequence of processing stages. |

---

# 20.8 Definition of Done

A development task is considered complete only when:

- Implementation completed.
- Local execution successful.
- Documentation updated (if required).
- Architecture remains consistent.
- Commit created.
- Changes pushed to GitHub.

Completion is determined by engineering quality, not only by functional correctness.

---

# 20.9 Future Expansion Principles

Future features should follow these principles:

- Extend existing architecture whenever appropriate.
- Preserve module independence.
- Avoid breaking established interfaces.
- Maintain backward compatibility where practical.
- Introduce new modules only when justified.

Examples of potential future extensions include:

- Incremental backup
- Differential backup
- Plugin system
- Web API
- Web Dashboard
- GUI application
- Docker deployment
- Cloud synchronization
- Scheduler
- Multi-user support

These features are intentionally outside the Version 1.0 scope.

---

# 20.10 Document Maintenance

PROJECT_CONTEXT.md is a living engineering document.

It should be reviewed whenever:

- A new architectural decision is accepted.
- A major module is introduced.
- The project workflow changes.
- The roadmap changes significantly.

Minor implementation changes generally do not require updates.

---

# 20.11 Closing Statement

This document represents the collective engineering decisions made throughout the development of the Ruijie Cloud Backup Toolkit (RCBT).

Its purpose is not only to describe the current system but also to preserve the reasoning, principles, and standards that guide future development.

Every future implementation should aim to strengthen the architecture rather than work around it.

The long-term success of the project depends on consistency, maintainability, and disciplined engineering practices.

---

**End of PROJECT_CONTEXT.md**

**Document Status:** Active

**Document Version:** 1.0

**Maintainer:** Ryan Fajar

**Project:** Ruijie Cloud Backup Toolkit (RCBT)

**Single Source of Truth:** This document

---
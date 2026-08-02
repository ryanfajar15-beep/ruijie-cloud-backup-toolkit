# PROJECT_CONTEXT.md

### Single Source of Truth (SSOT)
>
> This document defines the long-term engineering identity, architecture, design philosophy, engineering standards, governance, and implementation principles of the Ruijie Cloud Backup Toolkit (RCBT).
>
> Unlike SESSION_CONTEXT.md, this document intentionally excludes temporary development status, active tasks, current phases, Git metadata, roadmap progress, and other frequently changing information.
>
> PROJECT_CONTEXT.md should remain stable and evolve only when the project's architecture, engineering philosophy, or long-term design changes.

---

# 1. Document Information

| Item | Value |
|------|-------|
| Document | PROJECT_CONTEXT.md |
| Project | Ruijie Cloud Backup Toolkit (RCBT) |
| Document Type | Engineering Context Document |
| Status | FROZEN |
| Version | 2.0 |
| Language | English |
| Audience | Project Owner, Software Engineers, AI Assistants, Future Contributors |
| Priority | Highest |

---

# 3. Purpose

PROJECT_CONTEXT.md provides the engineering foundation of the Ruijie Cloud Backup Toolkit.

Its primary purpose is to preserve architectural consistency throughout the lifetime of the project.

Unlike implementation documentation, this document focuses on long-term engineering knowledge rather than temporary development activities.

The objectives are:

- Preserve engineering philosophy.
- Preserve architectural consistency.
- Preserve implementation principles.
- Preserve module responsibilities.
- Prevent architecture drift.
- Define project boundaries.
- Reduce onboarding time.
- Support future contributors.
- Support AI-assisted development.
- Ensure long-term maintainability.

Whenever implementation conflicts with this document, the conflict should be reviewed before implementation continues.

---

# 4. Project Overview

Ruijie Cloud Backup Toolkit (RCBT) is a production-grade engineering toolkit designed to understand, analyze, and automate Ruijie Cloud operations through structured reverse engineering.

The project began with HAR (HTTP Archive) analysis but has evolved into a modular engineering platform capable of discovering application behavior and transforming that knowledge into reusable runtime components.

RCBT is not intended to be a simple backup script.

Instead, it provides a structured engineering platform capable of:

- Reverse engineering Ruijie Cloud communication.
- Discovering authentication mechanisms.
- Building structured API knowledge.
- Managing cloud backup operations.
- Supporting future restore workflows.
- Generating engineering reports.
- Providing reusable runtime components.

The project prioritizes long-term maintainability over rapid implementation.

---

# 5. Vision

Create a production-grade engineering platform capable of completely understanding Ruijie Cloud communication while providing reliable, maintainable, and extensible backup automation.

The project aims to evolve beyond a backup utility into a reusable toolkit suitable for multiple customers, projects, and future cloud automation initiatives.

---

# 6. Engineering Philosophy

RCBT follows several long-term engineering principles.

## 6.1 Architecture First

Architecture always has higher priority than implementation speed.

Short-term solutions must never compromise long-term maintainability.

---

## 6.2 Single Responsibility

Every module owns one responsibility.

Responsibilities must never overlap.

Business logic must remain isolated.

---

## 6.3 Separation of Concerns

Filesystem management,
HAR parsing,
authentication,
API communication,
backup,
reporting,
and exporting

must remain independent.

Each subsystem communicates only through well-defined inputs and outputs.

---

## 6.4 Maintainability First

Readable, predictable, and maintainable code is preferred over clever or highly optimized implementations.

Engineering consistency always takes precedence over implementation shortcuts.

---

## 6.5 Incremental Engineering

Development progresses through small, validated, and documented phases.

Each completed phase becomes the stable foundation for subsequent work.

---

## 6.6 Documentation-Driven Engineering

Documentation is considered part of the implementation.

Major engineering decisions should be documented before significant implementation changes.

---

## 6.7 Git-Driven Development

Every significant engineering milestone should be preserved through Git.

Meaningful commits provide historical traceability and support long-term maintenance.

---

## 6.8 Production-Grade Quality

Every implementation should be designed with production quality in mind.

Temporary prototypes, experimental shortcuts, and project-specific hacks should be avoided whenever possible.

---

# End of Part 1

# 7. Project Goals

RCBT is developed as a long-term engineering platform rather than a single-purpose automation script.

The primary goals of the project are:

- Understand Ruijie Cloud communication.
- Reverse engineer undocumented APIs.
- Build structured API knowledge.
- Discover authentication workflows.
- Generate reusable endpoint metadata.
- Execute reliable backup operations.
- Support future restore capabilities.
- Produce engineering-grade reports.
- Support multiple independent customer projects.
- Maintain production-grade engineering quality.

Every implementation should contribute toward these goals.

---

# 8. Project Scope

RCBT focuses exclusively on engineering activities related to Ruijie Cloud.

The project scope includes:

- HAR analysis.
- HTTP request analysis.
- Authentication discovery.
- API discovery.
- API relationship mapping.
- Runtime metadata generation.
- Cloud resource backup.
- Future restore workflow.
- Structured reporting.
- Engineering documentation.
- Runtime automation.

The project is intended to become the engineering foundation for future Ruijie Cloud automation.

---

# 9. Non-Goals

To preserve architectural consistency, several items are intentionally excluded.

RCBT is **not** intended to become:

- A monolithic application.
- A collection of independent scripts.
- A GUI-first application.
- A one-off customer project.
- A manually operated workflow.
- A hardcoded automation script.
- A project-specific implementation.
- A replacement for official Ruijie Cloud services.

The following practices should also be avoided:

- Hardcoded endpoints.
- Hardcoded credentials.
- Business logic duplication.
- Tight coupling between modules.
- Hidden dependencies.
- Direct filesystem manipulation outside Workspace.
- Architecture changes without documentation.

---

# 10. Engineering Objectives

The engineering objectives guide every architectural decision throughout the project lifecycle.

The objectives are listed by priority.

## 10.1 Architectural Consistency

Maintain a predictable and modular architecture throughout the project.

Every implementation should reinforce the existing architecture rather than bypass it.

---

## 10.2 Maintainability

The project should remain understandable after years of development.

Readable code is preferred over compact code.

Predictable behavior is preferred over implicit behavior.

---

## 10.3 Reusability

Every module should be reusable by future modules.

Business logic should never depend on project-specific assumptions.

---

## 10.4 Scalability

The architecture should support future expansion without requiring major redesign.

New functionality should integrate into the existing architecture through well-defined interfaces.

---

## 10.5 Reliability

Every execution should produce deterministic and reproducible results.

Unexpected behavior should be minimized through explicit workflows and validation.

---

## 10.6 Extensibility

Future modules should integrate without requiring changes to existing components whenever practical.

Examples include:

- Restore Engine
- Knowledge Engine
- Plugin System
- Scheduler
- Web Dashboard
- Cloud Synchronization

---

# 11. Core Design Principles

The architecture follows several long-term design principles.

## 11.1 One Entry Point

Application execution begins from a single entry point.

Current implementation:

```text
backup.py
```

No module may replace the application entry point.

---

## 11.2 One Execution Pipeline

Every execution follows the same workflow.

The execution pipeline must remain deterministic.

Modules must never bypass mandatory stages.

---

## 11.3 One Responsibility

Every module owns one responsibility.

Business logic duplication is prohibited.

---

## 11.4 Explicit Data Flow

Every module communicates through explicit inputs and outputs.

Hidden dependencies should be avoided.

Global mutable state should be minimized.

---

## 11.5 Infrastructure Separation

Infrastructure concerns remain independent from business logic.

Examples of infrastructure responsibilities include:

- Workspace
- Configuration
- Logging
- Filesystem
- Session Storage

Business modules should consume infrastructure services without owning them.

---

## 11.6 Stable Interfaces

Public interfaces should remain stable whenever possible.

Breaking interface changes require engineering review.

---

## 11.7 Documentation Before Refactoring

Major refactoring should be documented before implementation begins.

Architectural reasoning is considered part of the implementation.

---

# 12. Long-Term Design Constraints

The following constraints define the long-term direction of the project.

## Constraint 1

There is only one application entry point.

---

## Constraint 2

Workspace exclusively owns project filesystem management.

---

## Constraint 3

Parser remains responsible only for interpreting HAR data.

---

## Constraint 4

Business modules never manipulate Workspace internals.

---

## Constraint 5

The Runtime Layer consumes structured metadata rather than raw implementation details whenever practical.

---

## Constraint 6

Dependencies always flow downward.

Reverse dependencies are prohibited.

---

## Constraint 7

Documentation evolves together with architecture.

Undocumented architectural changes are discouraged.

---

## Constraint 8

Engineering quality always has higher priority than implementation speed.

---

# End of Part 2

# 13. Repository Structure
The following structure represents the repository root.

```text
backup.py

development/
docs/
analysis/
projects/
incoming/
release/
tools/
tests/
```

| Path | Responsibility |
|------|----------------|
| `development/` | Core application modules |
| `docs/` | Engineering documentation |
| `analysis/` | Reverse engineering outputs |
| `projects/` | Generated workspaces |
| `incoming/` | HAR import directory |
| `release/` | Release artifacts |
| `tools/` | Development utilities |
| `tests/` | Automated testing |


This structure represents the repository root only.

Individual subsystem architectures are documented separately.

# 14. High-Level System Architecture

## 14.1 Architectural Overview

RCBT follows a layered modular architecture.

Each layer owns a single responsibility and communicates only through well-defined interfaces.

The architecture is designed to maximize maintainability, testability, scalability, and long-term evolution while minimizing coupling between modules.

Application execution always follows a deterministic processing pipeline.

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
                               v
                    +----------------------+
                    |     HAR Importer     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |     HAR Parser       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Discovery Engine     |
                    +----------+-----------+
                               |
                +--------------+--------------+
                |              |              |
                v              v              v
        Authentication     Endpoint      Workflow
          Discovery       Discovery      Discovery
                |              |              |
                +--------------+--------------+
                               |
                               v
                    +----------------------+
                    |     Runtime Layer    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |  Backup Workflow     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |    Report Layer      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |    Export Layer      |
                    +----------------------+
```

Every stage produces structured artifacts consumed by downstream modules.

No module should bypass the defined execution order.

---

# 14.2 Architecture Layers

The application is organized into multiple logical layers.

Each layer has clearly defined ownership.

---

## Application Layer

Purpose

Coordinate the entire execution.

Current component

```text
backup.py
```

Responsibilities

- Application startup
- Configuration loading
- Logging initialization
- Workflow orchestration
- Global exception handling
- Runtime coordination

---

## Workspace Layer

Purpose

Manage project lifecycle and filesystem ownership.

Responsibilities

- HAR discovery
- Workspace creation
- Project metadata
- Directory management
- Path resolution
- Workspace Context generation

Current implementation

```text
development/workspace/
```

---

## Parsing Layer

Purpose

Interpret HAR files.

Responsibilities

- HAR validation
- Request parsing
- Request normalization
- Parsed request generation

Current implementation

```text
development/parser/
```

---

## Discovery Layer

Purpose

Transform parsed requests into structured engineering knowledge.

Responsibilities

- Authentication Discovery
- Endpoint Discovery
- Workflow Discovery
- Request Classification
- Response Analysis

Discovery does not perform runtime operations.

---

## Runtime Layer

Purpose

Execute application behavior using structured discovery results.

Responsibilities

- Authentication Runtime
- API Runtime
- Download Runtime
- Backup Runtime
- Execution Control

Runtime never parses HAR directly.

---

## Report Layer

Purpose

Generate structured execution reports.

Responsibilities

- Execution summary
- Statistics
- Error reporting
- Runtime metrics

---

## Export Layer

Purpose

Generate distributable project artifacts.

Responsibilities

- JSON export
- HTML export
- CSV export
- ZIP packaging
- Future export formats

---

# 14.3 Architectural Principles

The architecture follows several mandatory principles.

## Layer Independence

Every layer owns one responsibility.

Business logic must not leak across architectural boundaries.

---

## Explicit Dependencies

Dependencies always flow downward.

```text
Main Controller
        │
        ▼
Workspace
        │
        ▼
Parser
        │
        ▼
Discovery Layer
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

Reverse dependencies are prohibited.

---

## Infrastructure Isolation

Infrastructure components remain isolated from business logic.

Infrastructure includes:

- Workspace
- Filesystem
- Configuration
- Logging

Business modules consume infrastructure but never own it.

---

## Reusable Components

Every module should remain reusable.

Modules should avoid assumptions about:

- filesystem layout
- runtime environment
- project-specific configuration

---

## Stable Contracts

Communication between modules occurs only through explicit contracts.

Preferred communication mechanisms include:

- Models
- Context Objects
- Structured Metadata
- Return Values

Global mutable state should be avoided.

---

# 14.4 Architectural Constraints

The following constraints define the architecture.

## One Entry Point

Application execution always begins from:

```text
backup.py
```

---

## One Workspace

Every execution belongs to exactly one Workspace.

---

## One Processing Pipeline

Every execution follows the same processing order.

Skipping stages is prohibited.

---

## Workspace Owns Infrastructure

Only Workspace manages project directories.

No other module may create project structures.

---

## Parser Remains Pure

Parser only interprets HAR.

Parser never performs:

- authentication
- download
- reporting
- workspace creation

---

## Discovery Produces Knowledge

Discovery transforms parsed requests into reusable metadata.

Discovery does not execute runtime behavior.

---

## Runtime Consumes Structured Metadata

The Runtime Layer consumes structured outputs produced by Discovery.

Runtime should remain independent from raw HAR data whenever practical.

---

# End of Part 3

# 15. Workspace Architecture

## 15.1 Purpose

The Workspace subsystem is responsible for managing the complete lifecycle of every project.

Its purpose is to transform an incoming HAR file into a fully isolated project workspace that can be processed independently by the remaining application modules.

Workspace is the only subsystem that owns project infrastructure.

All other modules consume Workspace Context without manipulating the underlying filesystem.

---

# 15.2 Responsibilities

Workspace owns the following responsibilities.

Infrastructure

- Detect incoming HAR files.
- Create project workspace.
- Generate project metadata.
- Create directory structure.
- Resolve project paths.
- Provide Workspace Context.

Project Lifecycle

- Initialize project.
- Prepare input files.
- Maintain project identity.
- Manage workspace status.

Workspace must never perform:

- HAR parsing.
- Authentication discovery.
- Endpoint discovery.
- Runtime execution.
- Backup logic.
- Report generation.

---

# 15.3 Workspace Lifecycle

Every project follows the same lifecycle.

```text
User Export HAR
        │
        ▼
incoming/
        │
        ▼
Workspace Detection
        │
        ▼
Workspace Creation
        │
        ▼
Project Metadata
        │
        ▼
Workspace Context
        │
        ▼
Processing Pipeline
```

Every project execution begins with Workspace initialization.

No downstream module should execute before Workspace has completed successfully.

---

# 15.4 Incoming Directory

The incoming directory is the official entry point for every HAR session.

Example

```text
incoming/

device_a.har

device_b.har

customer_c.har
```

Users only need to copy HAR files into this directory.

Workspace automatically discovers every supported HAR file.

Manual workspace creation is never required.

---

# 15.5 Workspace Creation

Each HAR file generates exactly one Workspace.

Example

```text
projects/

20260801_customer_a/
```

Workspace names should remain unique.

Recommended naming strategy

```text
YYYYMMDD_<project_name>
```

Example

```text
20260801_customer_a

20260801_customer_b

20260802_customer_c
```

Future naming strategies may evolve without affecting downstream modules.

---

# 15.6 Standard Workspace Structure

Every project follows the same directory layout.

```text
projects/
└── <project_name>/
    ├── project.json
    ├── input/
    │   └── session.har
    ├── analysis/
    ├── output/
    ├── report/
    ├── logs/
    └── runtime/
```

Every module should rely on Workspace Context rather than constructing filesystem paths manually.

The following structure represents a single project workspace,
not the repository root.

---

# 15.7 Workspace Metadata

Each Workspace contains a project metadata file.

```text
project.json
```

Typical metadata includes

- Project ID
- Project Name
- Creation Timestamp
- Source HAR
- Toolkit Version
- Workspace Status
- Processing Status

Future versions may extend this metadata without breaking compatibility.

---

# 15.8 Workspace Context

Workspace returns a standardized context object consumed by downstream modules.

Typical information includes

- Project Root
- Input Directory
- Analysis Directory
- Output Directory
- Report Directory
- Runtime Directory
- Log Directory
- Metadata Location
- HAR Location

Every downstream module should consume Workspace Context instead of manually resolving paths.

---

# 15.9 Filesystem Ownership

Workspace exclusively owns the project filesystem.

Workspace may

- Create directories.
- Move HAR files.
- Generate metadata.
- Resolve project paths.
- Prepare runtime directories.

Other modules must never

- Create project folders.
- Rename project directories.
- Move HAR files.
- Modify Workspace metadata.

Filesystem ownership must remain centralized.

---

# 15.10 Workspace Design Principles

Workspace follows the following principles.

Automatic over manual.

Convention over configuration.

Predictable directory layout.

Single filesystem owner.

Explicit project identity.

Stable project metadata.

Future scalability.

Minimal coupling.

---

# 15.11 Workspace Contracts

Workspace produces

- Workspace Context
- Project Metadata
- Project Structure

Workspace consumes

- HAR File

Workspace communicates only through explicit context objects.

No downstream module should depend on Workspace implementation details.

---

# 15.12 Future Expansion

The Workspace subsystem has been intentionally designed for future capabilities.

Potential future enhancements include

- Multiple Workspace management.
- Workspace indexing.
- Workspace search.
- Resume interrupted execution.
- Parallel Workspace execution.
- Workspace archiving.
- Incremental Workspace updates.
- Cloud Workspace synchronization.

Future expansion should preserve backward compatibility and existing Workspace contracts.

---

# End of Part 4

# 16. Processing Workflow & Data Flow

## 16.1 Purpose

The Processing Workflow defines the official execution lifecycle of the Ruijie Cloud Backup Toolkit (RCBT).

Its purpose is to ensure every execution follows a predictable, reproducible, and deterministic processing pipeline.

Each stage produces structured artifacts consumed by downstream modules.

No module should bypass the defined workflow.

---

# 16.2 Processing Pipeline

Every execution follows the same high-level pipeline.

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
 │
 ▼
Finished
```

Each stage has a clearly defined responsibility.

---

# 16.3 Execution Stages

## Stage 1 — HAR Acquisition

Input

```text
incoming/*.har
```

Responsibilities

- Detect HAR files.
- Validate file format.
- Ignore unsupported files.
- Prepare Workspace initialization.

Output

HAR Import Request.

---

## Stage 2 — Workspace Initialization

Input

HAR Import Request.

Responsibilities

- Create Workspace.
- Generate project metadata.
- Prepare directory structure.
- Move HAR into Workspace.
- Generate Workspace Context.

Output

Workspace Context.

---

## Stage 3 — HAR Parsing

Input

Workspace Context.

Responsibilities

- Read HAR.
- Validate HAR structure.
- Parse HTTP requests.
- Preserve chronological order.
- Normalize request data.

Output

Parsed Requests.

Parser performs no business logic.

---

## Stage 4 — Discovery

Input

Parsed Requests.

Responsibilities

- Discover Authentication.
- Discover Endpoints.
- Discover Workflow.
- Classify Requests.
- Analyze Responses.
- Build Discovery Metadata.

Output

Discovery Metadata.

Discovery is responsible only for understanding captured communication.

It never executes runtime operations.

---

## Stage 5 — Runtime Preparation

Input

Discovery Metadata.

Responsibilities

- Build Runtime Context.
- Prepare Authentication Runtime.
- Prepare API Runtime.
- Resolve Endpoint Metadata.
- Prepare Download Strategy.

Output

Runtime Context.

---

## Stage 6 — Backup Workflow

Input

Runtime Context.

Responsibilities

- Authenticate.
- Execute API Requests.
- Handle Pagination.
- Retry Failed Operations.
- Download Resources.
- Preserve Resource Hierarchy.

Output

Backup Artifacts.

---

## Stage 7 — Report Generation

Input

Execution Results.

Responsibilities

- Execution Summary.
- Runtime Statistics.
- Download Summary.
- Error Report.
- Processing Metrics.

Output

Report Artifacts.

---

## Stage 8 — Export

Input

Workspace Artifacts.

Responsibilities

- Package Results.
- Export Reports.
- Export Metadata.
- Generate Deliverables.

Supported outputs may include

- JSON
- HTML
- CSV
- ZIP

Output

Export Packages.

---

# 16.4 Artifact Flow

The following diagram illustrates how artifacts move throughout the pipeline.

```text
HAR
 │
 ▼
Workspace Context
 │
 ▼
Parsed Requests
 │
 ▼
Discovery Metadata
 │
 ▼
Runtime Context
 │
 ▼
Backup Artifacts
 │
 ▼
Reports
 │
 ▼
Export Packages
```

Each artifact has exactly one producer.

Each artifact may have multiple consumers.

---

# 16.5 Processing Contracts

Every processing stage produces explicit outputs.

## Workspace

Consumes

HAR.

Produces

Workspace Context.

---

## Parser

Consumes

Workspace Context.

Produces

Parsed Requests.

---

## Discovery

Consumes

Parsed Requests.

Produces

Discovery Metadata.

---

## Runtime

Consumes

Discovery Metadata.

Produces

Runtime Context.

---

## Backup Workflow

Consumes

Runtime Context.

Produces

Backup Artifacts.

---

## Report Layer

Consumes

Execution Results.

Produces

Reports.

---

## Export Layer

Consumes

Workspace Artifacts.

Produces

Export Packages.

---

# 16.6 Error Handling Strategy

Processing should stop immediately whenever a critical stage fails.

Critical failures include

- Missing HAR.
- Invalid HAR.
- Workspace initialization failure.
- Parser failure.
- Discovery failure.

Non-critical failures include

- Single resource download failure.
- Retry exhaustion.
- Partial export failure.
- Optional report generation failure.

Whenever practical, non-critical failures should be logged while allowing processing to continue.

---

# 16.7 Logging Strategy

Every stage should generate structured logs.

Each log entry should include

- Timestamp.
- Processing Stage.
- Module Name.
- Severity.
- Message.
- Exception Details (if applicable).

Logs should be stored under

```text
logs/
```

Future implementations may support

- Log Rotation.
- Multiple Log Levels.
- Structured JSON Logs.
- Centralized Logging.

---

# 16.8 Processing Principles

The processing workflow follows several principles.

- Sequential execution.
- Explicit artifacts.
- Deterministic behavior.
- Reproducible execution.
- Failure isolation.
- Explicit ownership.
- Immutable intermediate artifacts.
- Predictable processing order.

---

# 16.9 Runtime Principles

Runtime Layer should never perform discovery.

Runtime responsibilities are limited to execution.

Runtime should consume structured metadata produced by Discovery.

Whenever possible, Runtime should remain independent from raw HAR files.

This separation preserves maintainability and enables future Knowledge Engine integration without redesigning Runtime Layer.

---

# End of Part 5

# 17. Module Responsibilities

## 17.1 Purpose

This section defines the responsibility boundaries of every major module within the Ruijie Cloud Backup Toolkit (RCBT).

Each module owns exactly one primary responsibility.

Responsibilities must never overlap.

Whenever new functionality is introduced, it should be assigned to an existing module only if it belongs to that module's responsibility.

Otherwise, a new module should be introduced.

---

# 17.2 Main Controller

Location

```text
backup.py
```

Purpose

Coordinate the entire application lifecycle.

Responsibilities

- Application startup.
- Configuration loading.
- Logging initialization.
- Workflow orchestration.
- Workspace initialization.
- Global exception handling.
- Execution summary.

Must NOT

- Parse HAR.
- Execute Discovery.
- Execute Runtime logic.
- Download resources.
- Generate reports.

---

# 17.3 Workspace Module

Location

```text
development/workspace/
```

Purpose

Manage project lifecycle and infrastructure.

Responsibilities

- Detect HAR files.
- Create Workspace.
- Generate project metadata.
- Manage project paths.
- Move HAR files.
- Return Workspace Context.

Must NOT

- Parse HAR.
- Discover APIs.
- Authenticate users.
- Execute Runtime.
- Download resources.

Produces

```text
Workspace Context
```

---

# 17.4 Parser Module

Location

```text
development/parser/
```

Purpose

Interpret HAR files.

Responsibilities

- Validate HAR.
- Read requests.
- Normalize requests.
- Preserve execution order.
- Produce Parsed Requests.

Must NOT

- Create project directories.
- Authenticate.
- Discover APIs.
- Execute Runtime.
- Download resources.

Produces

```text
Parsed Requests
```

---

# 17.5 Discovery Engine

Purpose

Transform Parsed Requests into reusable engineering metadata.

Responsibilities

- Authentication Discovery.
- Endpoint Discovery.
- Workflow Discovery.
- Request Classification.
- Response Analysis.
- Metadata Generation.

Must NOT

- Execute Runtime.
- Download resources.
- Generate reports.
- Modify Workspace.

Produces

```text
Discovery Metadata
```

Consumes

```text
Parsed Requests
```

---

# 17.6 Runtime Module

Location

```text
development/runtime/
```

Purpose

Execute application behavior using structured discovery results.

Responsibilities

- Authentication Runtime.
- Session Management.
- API Execution.
- Download Preparation.
- Runtime Validation.
- Execution Context.

Must NOT

- Parse HAR.
- Discover Endpoints.
- Create Workspace.
- Generate Reports.

Produces

```text
Runtime Context
```

Consumes

```text
Discovery Metadata
```

---

# 17.7 Backup Workflow

Location

```text
development/workflow/
```

Purpose

Coordinate backup execution.

Responsibilities

- Execute Backup Pipeline.
- Coordinate Runtime.
- Handle Retry Logic.
- Handle Pagination.
- Preserve Resource Structure.
- Generate Execution Results.

Must NOT

- Parse HAR.
- Discover APIs.
- Modify Workspace.

Produces

```text
Backup Artifacts
```

Consumes

```text
Runtime Context
```

---

# 17.8 Report Layer

Location

```text
development/report/
```

Purpose

Generate execution reports.

Responsibilities

- Execution Summary.
- Download Summary.
- Error Summary.
- Statistics.
- Runtime Metrics.

Produces

```text
Reports
```

Consumes

```text
Execution Results
```

---

# 17.9 Export Layer

Location

```text
development/exporter/
```

Purpose

Generate distributable artifacts.

Responsibilities

- JSON Export.
- HTML Export.
- CSV Export.
- ZIP Packaging.
- Future Export Formats.

Produces

```text
Export Packages
```

Consumes

```text
Workspace Artifacts
```

---

# 17.10 Shared Models

Modules should communicate using shared models instead of internal implementation details.

Typical shared models include

```text
WorkspaceContext

ParsedRequest

DiscoveryMetadata

RuntimeContext

ExecutionResult

BackupArtifact

ExportPackage
```

Shared models reduce coupling and improve maintainability.

---

# 17.11 Dependency Rules

Dependencies always flow downward.

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
Discovery Layer
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

Reverse dependencies are prohibited.

Examples

Parser must never import Workspace.

Workspace must never import Runtime.

Discovery must never import Main Controller.

Runtime must never import Parser.

Report must never import Runtime.

Exporter must never import Parser.

---

# 17.12 Responsibility Matrix

| Module | Infrastructure | Business Logic | Primary Output |
|---------|----------------|----------------|----------------|
| Main Controller | ❌ | Orchestration | Execution Pipeline |
| Workspace | ✅ | Project Lifecycle | Workspace Context |
| Parser | ❌ | HAR Interpretation | Parsed Requests |
| Discovery | ❌ | Reverse Engineering | Discovery Metadata |
| Runtime | ❌ | Runtime Execution | Runtime Context |
| Backup Workflow | ❌ | Backup Execution | Backup Artifacts |
| Report | ❌ | Reporting | Reports |
| Export | ❌ | Packaging | Export Packages |

---

# 17.13 Engineering Principles

Every module should satisfy the following principles.

- Single Responsibility.
- Explicit Input.
- Explicit Output.
- No Hidden Dependencies.
- No Filesystem Ownership except Workspace.
- No Business Logic Duplication.
- Easy to Test.
- Easy to Replace.
- Easy to Extend.
- Production Ready.

Whenever a module grows beyond its primary responsibility, it should be evaluated for decomposition into smaller components.

---

# End of Part 6

# 18. Engineering Standards

## 18.1 Purpose

Engineering Standards define the minimum quality requirements for every implementation within the Ruijie Cloud Backup Toolkit (RCBT).

These standards ensure that the project remains maintainable, scalable, and production-ready throughout its lifecycle.

Every implementation should comply with these standards before being considered complete.

---

# 18.2 Coding Standards

Every implementation should follow consistent engineering practices.

Requirements

- Production-ready implementation.
- Readable code.
- Explicit naming.
- Strong typing whenever practical.
- Small, focused modules.
- Explicit exception handling.
- Minimal side effects.
- Deterministic behavior.

Avoid

- Hidden dependencies.
- Implicit behavior.
- Hardcoded values.
- Business logic duplication.
- Circular imports.
- Global mutable state.

---

# 18.3 Design Standards

The architecture should remain modular.

Preferred characteristics

- Single Responsibility Principle.
- Separation of Concerns.
- Dependency Isolation.
- Explicit Interfaces.
- Composition over inheritance.
- Configuration-driven behavior.

Every design decision should improve maintainability rather than increase implementation speed.

---

# 18.4 Configuration Standards

Configuration must remain external to business logic.

Configuration includes

- API Endpoints.
- Credentials.
- Runtime Options.
- Directory Locations.
- Feature Flags.
- Timeout Values.

Configuration must never be hardcoded inside business modules.

---

# 18.5 Error Handling Standards

Errors should be handled explicitly.

Each exception should

- Describe the problem.
- Preserve debugging information.
- Support structured logging.
- Allow graceful recovery whenever practical.

Unexpected exceptions should never be silently ignored.

---

# 18.6 Logging Standards

Logging should provide enough information to reproduce problems.

Every significant operation should include

- Timestamp.
- Module Name.
- Processing Stage.
- Severity.
- Message.
- Context Information.

Logs should support future troubleshooting without requiring source code inspection.

---

# 18.7 Documentation Standards

Documentation is considered part of the implementation.

Every significant engineering change should update the appropriate documentation.

Examples

- Architecture changes.
- Workflow changes.
- New modules.
- Engineering decisions.
- Phase completion.
- Breaking changes.

Documentation must remain synchronized with implementation.

---

# 18.8 Git Standards

Git history should represent engineering history.

Every commit should

- Be meaningful.
- Be traceable.
- Describe a logical unit of work.
- Preserve engineering milestones.

Avoid

- Large unrelated commits.
- Temporary commits.
- Unclear commit messages.

---

# 19. Quality Standards

Every implementation should satisfy the following quality attributes.

## Maintainability

The implementation should remain understandable by future contributors.

---

## Readability

Code should communicate intent clearly.

---

## Reliability

Execution should produce deterministic results.

---

## Scalability

Future expansion should not require architectural redesign.

---

## Reusability

Modules should be reusable whenever practical.

---

## Testability

Components should support isolated testing.

---

## Observability

Execution should provide sufficient information for debugging and monitoring.

---

## Backward Compatibility

Existing behavior should remain stable unless explicitly changed.

Breaking changes require engineering review.

---

# 20. Engineering Decision Process

Major engineering decisions should follow a structured process.

```text
Problem
        │
        ▼
Investigation
        │
        ▼
Alternative Solutions
        │
        ▼
Decision
        │
        ▼
Implementation
        │
        ▼
Documentation
```

Significant architectural decisions should be documented as ADR (Architecture Decision Record).

---

# 21. Documentation Governance

Every document has a specific responsibility.

| Document | Primary Responsibility |
|----------|----------------|
| CHAT_BOOTSTRAP.md | AI Working Rules & Engineering Constitution |
| SESSION_CONTEXT.md | Current Project Snapshot |
| PROJECT_CONTEXT.md | Long-term Engineering Context |
| ARCHITECTURE.md | System Architecture |
| ROADMAP.md | Development Roadmap |
| CHANGELOG.md | Engineering History |
| TODO.md | Engineering Task Tracker |
| HISTORY/ | Phase Documentation |
| DECISIONS/ | Architecture Decision Records |
| TROUBLESHOOTING/ | Engineering Knowledge Base |

Information should always be stored in the document responsible for that information.

Avoid duplicating information across multiple documents.


---

# 22. AI-Assisted Development

AI is considered an engineering partner.

AI should

- Preserve architecture.
- Preserve documentation quality.
- Preserve engineering consistency.
- Respect module responsibilities.
- Follow repository workflow.
- Avoid assumptions.
- Recommend improvements with justification.
- Produce reproducible implementations.
- Respect documented engineering decisions (ADR).

AI should not

- Change architecture without justification.
- Introduce unnecessary abstractions.
- Duplicate business logic.
- Bypass engineering workflow.
- Generate incomplete implementations.

---

# End of Part 7

# 23. Long-Term Architecture Direction

RCBT has been intentionally designed as an extensible engineering platform.

The architecture should evolve through well-defined phases while preserving backward compatibility and engineering consistency.

Future capabilities may include:

- Knowledge Engine
- Restore Runtime
- Plugin System
- Scheduler
- Multi-Project Management
- Parallel Execution
- Cloud Synchronization
- Web Dashboard
- API Service
- Continuous Backup
- Incremental Backup
- Distributed Processing

Future expansion should integrate into the existing architecture without requiring major redesign.

---

# 24. Scalability Strategy

RCBT should scale in multiple dimensions.

## Functional Scalability

Support additional Ruijie Cloud services without changing existing architecture.

---

## Customer Scalability

Support multiple customers while maintaining complete project isolation.

---

## Engineering Scalability

Support future contributors without increasing architectural complexity.

---

## Runtime Scalability

Allow future optimization such as:

- Parallel processing
- Queue-based execution
- Distributed workloads
- Incremental execution

without changing module responsibilities.

---

# 25. Maintainability Strategy

Long-term maintainability is one of the primary engineering objectives.

Maintainability is achieved through:

- Modular architecture.
- Single Responsibility Principle.
- Explicit interfaces.
- Stable contracts.
- Documentation-driven engineering.
- Consistent coding standards.
- Predictable workflows.
- Reproducible implementations.

Engineering consistency is always preferred over implementation shortcuts.

---

# 26. Engineering Principles Summary

Every engineering decision should support the following principles.

## Architecture

- Architecture First.
- Separation of Concerns.
- Single Responsibility.
- Explicit Dependencies.
- Stable Interfaces.

---

## Development

- Documentation-Driven Engineering.
- Git-Driven Development.
- Incremental Development.
- Production-Ready Implementation.

---

## Quality

- Maintainability.
- Scalability.
- Reliability.
- Testability.
- Observability.
- Backward Compatibility.

---

## Governance

- Explicit Ownership.
- Reproducible Development.
- Engineering Traceability.
- Long-Term Consistency.

---

# 27. Engineering Commitment

Every implementation within RCBT should contribute toward the long-term health of the project.

Engineering decisions should always consider:

- Architectural impact.
- Maintainability.
- Scalability.
- Future extensibility.
- Backward compatibility.
- Documentation consistency.

Temporary solutions should never become permanent architecture.

When trade-offs are unavoidable, they should be documented through Engineering Decisions (ADR).

---

# 28. Closing Statement

PROJECT_CONTEXT.md defines the engineering identity of the Ruijie Cloud Backup Toolkit.

It exists to preserve architectural consistency, engineering quality, and long-term maintainability throughout the lifetime of the project.

This document intentionally avoids storing information that changes frequently.

Dynamic project information belongs to dedicated documents such as:

- SESSION_CONTEXT.md
- ROADMAP.md
- CHANGELOG.md
- TODO.md
- HISTORY/
- DECISIONS/
- TROUBLESHOOTING/

Whenever implementation changes the long-term architecture, engineering philosophy, or project identity, this document should be reviewed and updated.

PROJECT_CONTEXT.md should remain stable throughout the lifetime of the project and should not be modified as part of routine engineering work.

---

# Document Maintenance Policy

PROJECT_CONTEXT.md should only be updated when one or more of the following changes occur:

- Engineering philosophy changes.
- Core architecture changes.
- Module responsibility changes.
- Long-term design principles change.
- Engineering governance changes.
- System boundaries change.

Routine engineering activities must update only:

- SESSION_CONTEXT.md
- TODO.md
- CHANGELOG.md
- ROADMAP.md

Routine development progress must never require updates to PROJECT_CONTEXT.md.

PROJECT_CONTEXT.md should only change when the long-term engineering identity evolves.

---

# 30. Document Status

| Item | Value |
|------|-------|
| Version | 2.0 |
| Status | Frozen |
| Update Policy | Architecture Changes Only |
| Maintained By | Project Owner & AI Engineering Partner |
| Engineering Model | Production-Grade Development |
| Classification | Engineering Context (Long-Term) |
| Primary Source of Truth | Repository Source Code |

Supporting engineering documents are authoritative only within their respective responsibilities defined by this document.

- CHAT_BOOTSTRAP.md
- SESSION_CONTEXT.md
- ARCHITECTURE.md
- ROADMAP.md
- CHANGELOG.md
- TODO.md
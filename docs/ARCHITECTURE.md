# RCBT ARCHITECTURE

> This document defines the technical architecture of the Ruijie Cloud Backup Toolkit (RCBT).
>
> Unlike PROJECT_CONTEXT.md, which defines long-term engineering identity and governance, this document describes how the architecture is implemented, how modules communicate, and how the execution flow operates.
>
> ARCHITECTURE.md should evolve only when the system architecture, processing workflow, or implementation design changes.

---

# 1. Document Information

| Item | Value |
|------|-------|
| Document | ARCHITECTURE.md |
| Project | Ruijie Cloud Backup Toolkit (RCBT) |
| Document Type | Technical Architecture Document |
| Primary Responsibility | Technical Implementation Architecture |
| Status | FREZZE |
| Version | 3.0 |
| Language | English |
| Audience | Software Engineers, AI Assistants, Future Contributors |
| Priority | High |

---

# 2. Purpose

ARCHITECTURE.md defines the implementation architecture of the Ruijie Cloud Backup Toolkit (RCBT).

Its purpose is to document how the system is organized internally, how architectural layers communicate, and how data moves through the application from start to finish.

Unlike PROJECT_CONTEXT.md, which defines long-term engineering identity and architectural direction, this document specifies the concrete implementation architecture that every module must follow.

This document serves as the primary technical reference for:

- Execution Flow
- Layer Communication
- Execution Context Objects
- Module Dependencies
- Runtime Boundaries
- Architectural Contracts

ARCHITECTURE.md intentionally focuses on implementation design rather than project planning, engineering governance, or development progress.

Whenever architectural implementation changes, this document should be updated before implementation diverges from the documented design.

---

# 3. Scope

ARCHITECTURE.md defines the technical implementation architecture of RCBT.

This document describes how architectural components interact, how information flows between modules, and how the application executes from initialization to completion.

The scope of this document includes:

- Repository Architecture
- Layered System Architecture
- Execution Flow
- Module Interaction
- Execution Context Objects
- Data Transformation
- Dependency Rules
- Runtime Execution Model
- Extension Points

This document intentionally excludes:

- Engineering governance
- Long-term project vision
- Development roadmap
- Current implementation status
- Active tasks
- Temporary technical decisions
- Engineering history

Those subjects are documented in:

| Document | Responsibility |
|----------|----------------|
| PROJECT_CONTEXT.md | Engineering Identity |
| SESSION_CONTEXT.md | Current Project State |
| ROADMAP.md | Future Development Plan |
| CHANGELOG.md | Engineering History |
| TODO.md | Active Development Tasks |
| DECISIONS/ | Architecture Decision Records |
| HISTORY/ | Phase History |
| TROUBLESHOOTING/ | Error Investigation History |

The purpose of this separation is to ensure that ARCHITECTURE.md remains a stable technical reference focused exclusively on implementation architecture.

---

# 4. Relationship with Other Documents

| Document | Responsibility |
|----------|----------------|
| CHAT_BOOTSTRAP.md | AI Working Rules |
| PROJECT_CONTEXT.md | Long-Term Engineering Context |
| ARCHITECTURE.md | Technical System Architecture |
| SESSION_CONTEXT.md | Current Project Status |
| API_DISCOVERY.md | Discovery Engine Specification |
| ROADMAP.md | Development Roadmap |
| CHANGELOG.md | Engineering History |

Whenever architectural implementation changes, this document should be updated before implementation diverges from the documented design.


---

# 5. System Overview

## 5.1 Overview

The Ruijie Cloud Backup Toolkit (RCBT) is a layered automation system designed to transform captured Ruijie Cloud communication into a structured, repeatable, and maintainable backup process.

Rather than executing directly from HAR files, RCBT separates analysis from execution by introducing a Discovery Engine and Runtime Layer.

This separation allows the toolkit to evolve independently from captured network traffic while preserving deterministic execution.

---

## 5.2 High-Level System Overview

```text
                        User
                         │
                         ▼
                    backup.py
               (Main Controller)
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
```

Each component performs one well-defined responsibility.

Modules communicate only through structured Execution Context Objects.

No component bypasses another architectural layer.

---

## 5.3 System Characteristics

RCBT has been designed with the following architectural characteristics.

- Deterministic execution
- Layered architecture
- Modular implementation
- Explicit module communication
- Clear separation of responsibilities
- Context-driven execution
- Extensible Execution Flow

---

## 5.4 Architectural Principles

The overall system follows several mandatory principles.

### Single Entry Point

All executions begin from:

```text
backup.py
```

No module should become an alternative application entry point.

---

### Layer Isolation

Each architectural layer owns one responsibility.

Business logic duplication between layers is prohibited.

---

### Explicit Communication

Modules communicate only through Execution Context Objects.

Direct access to another module's internal implementation is prohibited.

---

### Deterministic Processing

Every execution follows the same Execution Flow.

Execution order must remain predictable and reproducible.

---

### Discovery Before Runtime

Application behavior is analyzed only once during Discovery.

Runtime executes exclusively from structured Discovery Metadata.

---

### Runtime Before Workflow

Backup Workflow consumes RuntimeContext.

Workflow must never perform Discovery or HAR parsing.

---

### Report Before Export

Export Layer packages artifacts produced by the Report Layer.

Export never regenerates reports or reprocesses execution data.

---

## 5.5 Architectural Boundaries

The following responsibilities are intentionally outside the scope of the architecture.

- Engineering governance
- Development planning
- Current implementation status
- Temporary engineering decisions
- Git workflow
- Project roadmap

Those subjects are documented in their respective engineering documents.


---

# 6. Repository Architecture

## 6.1 Overview

The RCBT repository is organized to separate application logic, engineering documentation, project data, development utilities, and generated artifacts.

Each top-level directory owns one primary responsibility.

The repository structure is intentionally designed to support modular development, predictable maintenance, and long-term scalability.

---

## 6.2 Repository Structure

```text
ruijie-cloud-backup/
│
├── backup.py
│
├── development/
├── analysis/
├── docs/
├── incoming/
├── projects/
├── release/
├── tests/
└── tools/
```

The repository structure should remain stable unless an architectural change has been formally approved.

---

## 6.3 Top-Level Directory Responsibilities

| Directory | Responsibility |
|------------|----------------|
| backup.py | Main application entry point |
| development/ | Application source code |
| analysis/ | Discovery outputs and analysis artifacts |
| docs/ | Engineering documentation |
| incoming/ | Original HAR files awaiting project initialization |
| projects/ | Generated project workspaces |
| release/ | Release packages and distributions |
| tests/ | Automated testing |
| tools/ | Development utilities and automation scripts |

`incoming/` stores original HAR files before processing.

After successful workspace initialization, the HAR file is moved into the corresponding project workspace. If processing fails, the original HAR file remains in `incoming/` for investigation or retry.

---

## 6.4 Development Module Structure

The `development/` directory contains the application's implementation modules.

```text
development/
│
├── auth/
├── config/
├── parser/
├── report/
├── workflow/
├── workspace/
│
├── discovery/
├── runtime/
└── exporter/
```

Each module represents one architectural responsibility.

Modules should remain independent whenever possible.

---

## 6.5 Module Responsibilities

| Module | Responsibility |
|---------|----------------|
| auth/ | Authentication services |
| config/ | Configuration management |
| parser/ | HAR parsing and normalization |
| workspace/ | Workspace lifecycle management |
| workflow/ | Backup execution workflow |
| report/ | Report generation |
| discovery/ | Discovery Engine |
| runtime/ | Runtime Layer |
| exporter/ | Export Layer |

The `development/workspace/` module implements the architectural **Workspace** component and is responsible for Workspace initialization and lifecycle management.

Business logic should remain inside its corresponding module.

Cross-module implementation is discouraged.

---

## 6.6 Repository Design Principles

The repository follows several engineering principles.

### Single Responsibility

Every directory owns one primary responsibility.

---

### Predictable Structure

Directory names should remain stable across releases.

---

### Clear Separation

Infrastructure, implementation, documentation, testing, and generated data remain physically separated.

---

### Future Expansion

New modules should be added without restructuring existing directories whenever possible.

---

### Backward Compatibility

Repository changes should preserve compatibility with previous project structures whenever practical.

---

# 7. System Architecture

## 7.1 Overview

RCBT follows a layered architecture in which each layer owns a single architectural responsibility.

Each layer communicates only with its adjacent downstream layer through explicit Execution Context Objects.

This design minimizes coupling, improves maintainability, and enables independent evolution of individual subsystems.

No layer should bypass another layer or access internal implementation details outside its defined contract.

---

## 7.2 Architecture Layers

```text
                    Application Layer
                           │
                           ▼
                  Infrastructure Layer
                           │
                           ▼
                   Discovery Layer
                           │
                           ▼
                    Runtime Layer
                           │
                           ▼
                   Workflow Layer
                           │
                           ▼
                    Report Layer
                           │
                           ▼
                    Export Layer
```

Each layer owns one architectural responsibility.

Business logic must remain inside its corresponding layer.

---

## 7.3 Layer Overview

| Layer | Primary Responsibility |
|--------|------------------------|
| Application Layer | Application startup and workflow orchestration |
| Infrastructure Layer | Workspace, configuration, filesystem, logging |
| Discovery Layer | Analyze HAR and generate DiscoveryMetadata |
| Runtime Layer | Execute application behavior using DiscoveryMetadata |
| Workflow Layer | Coordinate backup execution |
| Report Layer | Generate execution reports |
| Export Layer | Package deliverables into distributable formats |

The Discovery Layer is primarily implemented by the Discovery Engine.

---

## 7.4 Layer Communication

Architectural layers communicate only through structured Execution Context Objects.

```text
Application
        │
        ▼
WorkspaceContext
        │
        ▼
ParsedRequests
        │
        ▼
DiscoveryMetadata
        │
        ▼
RuntimeContext
        │
        ▼
ExecutionResults
        │
        ▼
ReportArtifacts
        │
        ▼
ExportPackage
```

Direct communication between non-adjacent layers is prohibited.

## 7.5 Layer Responsibilities

### Application Layer

Responsible for:

- Application startup
- Workflow orchestration
- Global configuration
- Exception handling

Owns:

```text
backup.py
```

---

### Infrastructure Layer

Responsible for:

- Workspace management
- Configuration management
- Filesystem abstraction
- Logging
- Project initialization

Owns:

```text
development/workspace/
development/config/
```

---

### Discovery Layer

Responsible for:

- Authentication Discovery
- Endpoint Discovery
- Workflow Discovery
- Request Analysis
- Response Analysis
- Discovery Metadata generation

Consumes:

```text
ParsedRequests
```

Produces:

```text
DiscoveryMetadata
```

---

### Runtime Layer

Responsible for:

- Session management
- Authentication runtime
- Endpoint resolution
- API execution
- Runtime Context generation

Consumes:

```text
DiscoveryMetadata
```

Produces:

```text
RuntimeContext
```

---

### Workflow Layer

Responsible for:

- Backup orchestration
- Download coordination
- Retry strategy
- Pagination handling
- Execution sequencing

Consumes:

```text
RuntimeContext
```

Produces:

```text
ExecutionResults
```

---

### Report Layer

Responsible for:

- Execution reports
- Runtime statistics
- Error reports
- Processing metrics

Consumes:

```text
ExecutionResults
```

Produces:

```text
ReportArtifacts
```

---

### Export Layer

Responsible for:

- JSON export
- HTML export
- CSV export
- ZIP packaging

Consumes:

```text
ReportArtifacts
```

Produces:

```text
ExportPackage
```


## 7.6 Architectural Constraints

The following rules are mandatory.

### One Responsibility Per Layer

Each layer owns exactly one architectural responsibility.

---

### One Direction of Communication

Dependencies always flow downward.

Reverse dependencies are prohibited.

---

### Explicit Contracts

Layers communicate only through standardized Execution Context Objects.

Implementation details must remain private.

---

### Layer Isolation

No layer may access another layer's internal implementation directly.

Communication must occur only through public interfaces.

---

### Discovery Before Runtime

Discovery always completes before Runtime begins.

Runtime never analyzes HAR files.

---

### Runtime Before Workflow

Workflow consumes RuntimeContext.

Workflow never performs Discovery.

---

### Report Before Export

Export packages artifacts produced by the Report Layer.

Export never regenerates reports.

---

## 7.7 Architecture Summary

The layered architecture ensures that every subsystem has a clearly defined responsibility, predictable communication model, and explicit dependency direction.

This architecture enables independent development of future capabilities such as the Knowledge Engine, Restore Runtime, Scheduler, Plugin System, and Web Dashboard without requiring structural changes to the existing implementation.

---

# 8. Execution Flow

## 8.1 Overview

The Execution Flow defines the official execution lifecycle of RCBT.

Every execution follows the same deterministic sequence from HAR import to export generation.

Each processing stage produces structured outputs that become the input for the next stage.

Execution stages must never be skipped or reordered.

---

## 8.2 Complete Execution Flow

```text
                     User
                      │
                      ▼
                Select HAR File
                      │
                      ▼
                 Workspace
                      │
                      ▼
                 ImportedHAR
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
                 Execution End
```

The Execution Flow is strictly sequential.

Each stage must complete successfully before the next stage begins.

---

## 8.3 Execution Stages

| Stage | Input | Output |
|--------|-------|--------|
| Workspace | HAR File | WorkspaceContext |
| HAR Importer | WorkspaceContext | ImportedHAR |
| HAR Parser | ImportedHAR | ParsedRequests |
| Discovery Engine | ParsedRequests | DiscoveryMetadata |
| Runtime Layer | DiscoveryMetadata | RuntimeContext |
| Backup Workflow | RuntimeContext | ExecutionResults |
| Report Layer | ExecutionResults | ReportArtifacts |
| Export Layer | ReportArtifacts | ExportPackage |

---

## 8.4 Stage Dependencies

Every processing stage depends exclusively on the output produced by its immediate predecessor.

```text
Workspace
        │
        ▼
WorkspaceContext
        │
        ▼
HAR Importer
        │
        ▼
ImportedHAR
        │
        ▼
HAR Parser
        │
        ▼
ParsedRequests
        │
        ▼
DiscoveryMetadata
        │
        ▼
RuntimeContext
        │
        ▼
ExecutionResults
        │
        ▼
ReportArtifacts
        │
        ▼
ExportPackage
```

No stage should consume intermediate data produced by non-adjacent stages.

---

## 8.5 Execution Characteristics

The Execution Flow follows these architectural characteristics.

### Deterministic

The same input always produces the same execution sequence.

---

### Sequential

Processing stages execute in a predefined order.

Parallel execution may be introduced in future implementations without changing the logical execution flow.

---

### Reproducible

Execution flow should be reproducible across environments.

---

### Context-Driven

Each stage consumes Execution Context Objects instead of accessing internal module implementations.

---

### Layer Independent

Execution stages remain independent from each other.

Communication occurs only through standardized outputs.

---

## 8.6 Execution Contracts

Each processing stage must satisfy the following contract.

- Accept only the expected input object.
- Validate the received input.
- Produce a standardized output.
- Never modify outputs produced by previous stages.
- Report failures using standardized error handling.

This contract ensures predictable execution throughout the entire processing lifecycle.

---

## 8.7 Execution Summary

The Execution Flow represents the official execution model of RCBT.

All application executions, regardless of future features or supported services, must follow this processing sequence to preserve architectural consistency and predictable behavior.

---

# 9. Module Interaction

## 9.1 Overview

Module Interaction defines how architectural components communicate throughout the execution lifecycle.

Rather than accessing each other's internal implementation, modules exchange standardized Execution Context Objects.

This communication model reduces coupling while improving maintainability, scalability, and testability.

---

## 9.2 Interaction Sequence

```text
                     backup.py
                          │
                          │ starts
                          ▼
                Workspace
                          │
                          │ returns
                          ▼
                WorkspaceContext
                          │
                          │ passed to
                          ▼
                   HAR Importer
                          │
                          │ returns
                          ▼
                   ImportedHAR
                          │
                          │ passed to
                          ▼
                    HAR Parser
                          │
                          │ returns
                          ▼
                 ParsedRequests
                          │
                          │ passed to
                          ▼
                Discovery Layer
                          │
                          │ returns
                          ▼
                DiscoveryMetadata
                          │
                          │ passed to
                          ▼
                  Runtime Layer
                          │
                          │ returns
                          ▼
                  RuntimeContext
                          │
                          │ passed to
                          ▼
                 Backup Workflow
                          │
                          │ returns
                          ▼
                 ExecutionResults
                          │
                          │ passed to
                          ▼
                   Report Layer
                          │
                          │ returns
                          ▼
                  ReportArtifacts
                          │
                          │ passed to
                          ▼
                   Export Layer
                          │
                          │ returns
                          ▼
                  ExportPackage
```

---

## 9.3 Communication Contracts

Every module communicates through explicit outputs.

Modules must never depend on another module's internal implementation.

Each interaction consists of:

- Input Context
- Processing Logic
- Output Context

This contract ensures predictable communication across all architectural layers.

---

## 9.4 Interaction Rules

The following rules apply to all module interactions.

### Explicit Communication

Every module exchanges standardized Execution Context Objects.

---

### No Hidden Dependencies

Modules must never access private objects owned by another module.

---

### One Producer

Each Context Object has exactly one producer.

---

### Multiple Consumers

A Context Object may be consumed by one or more downstream modules.

---

### Immutable Outputs

After a Context Object has been produced, it must not be modified by downstream modules.

---

## 9.5 Interaction Summary

The interaction model ensures that every architectural component remains independent while participating in a predictable processing workflow.

Communication always occurs through explicit contracts rather than direct implementation coupling.

---

# 10. Execution Context Objects

## 10.1 Overview

Execution Context Objects define the official communication contract between architectural layers.

Instead of exposing implementation details, each module exchanges standardized Execution Context Objects that describe the current execution state.

This communication model minimizes coupling while allowing each module to evolve independently.

---

## 10.2 Context Lifecycle

```text
WorkspaceContext
        │
        ▼
ParsedRequests
        │
        ▼
DiscoveryMetadata
        │
        ▼
RuntimeContext
        │
        ▼
ExecutionResults
        │
        ▼
ReportArtifacts
        │
        ▼
ExportPackage
```

Each Context Object is produced exactly once and consumed by one or more downstream modules.

---

## 10.3 WorkspaceContext

Produced by

```text
Workspace
```

Consumed by

- HAR Importer

Typical information

- Workspace ID
- Project Name
- Project Root
- HAR Location
- Analysis Directory
- Runtime Directory
- Report Directory
- Output Directory

---

## 10.4 ParsedRequests

Produced by

```text
HAR Parser
```

Consumed by

```text
Discovery Layer
```

Typical information

- Request Order
- HTTP Method
- URL
- Headers
- Query Parameters
- Request Body
- Response Body
- Timestamp

---

## 10.5 DiscoveryMetadata

Produced by

```text
Discovery Layer
```

Consumed by

```text
Runtime Layer
```

Typical information

- Authentication Metadata
- Endpoint Metadata
- Workflow Metadata
- API Relationships
- Response Relationships

DiscoveryMetadata becomes the primary engineering knowledge consumed by the Runtime Layer.

---

## 10.6 RuntimeContext

Produced by

```text
Runtime Layer
```

Consumed by

```text
Backup Workflow
```

Typical information

- Session State
- Authentication Tokens
- Endpoint Mapping
- Runtime Configuration
- Download Strategy
- Execution Parameters

---

## 10.7 ExecutionResults

Produced by

```text
Backup Workflow
```

Consumed by

```text
Report Layer
```

Typical information

- Execution Summary
- Download Results
- Runtime Metrics
- Processing Statistics
- Error Collection

---

## 10.8 ReportArtifacts

Produced by

```text
Report Layer
```

Consumed by

```text
Export Layer
```

Typical information

- Summary Report
- Runtime Report
- Error Report
- Metrics Report

---

## 10.9 Context Principles

Every Context Object follows these principles.

- One producer
- Multiple downstream consumers
- Immutable after creation
- Explicit ownership
- Standardized structure
- No business logic

Execution Context Objects are the only supported communication mechanism between architectural layers.


# 11. Data Transformation

## 11.1 Overview

Data Transformation defines how information is transformed throughout the RCBT architecture.

Unlike the Execution Flow, which describes execution order, Data Transformation describes how structured data moves between architectural layers.

Each layer consumes one standardized input and produces one standardized output.

---

## 11.2 Data Transformation Model

```text
HAR File
        │
        ▼
WorkspaceContext
        │
        ▼
ParsedRequests
        │
        ▼
DiscoveryMetadata
        │
        ▼
RuntimeContext
        │
        ▼
ExecutionResults
        │
        ▼
ReportArtifacts
        │
        ▼
ExportPackage
```

Every transformation creates a new architectural object.

Previously generated objects remain unchanged.

---

## 11.3 Data Ownership

| Data Object | Owner |
|-------------|-------|
| HAR File | User / External Input |
| WorkspaceContext | Workspace |
| ImportedHAR | HAR Importer |
| ParsedRequests | HAR Parser |
| DiscoveryMetadata | Discovery Layer |
| RuntimeContext | Runtime Layer |
| ExecutionResults | Backup Workflow |
| ReportArtifacts | Report Layer |
| ExportPackage | Export Layer |

Ownership is exclusive.

Only the producing layer may modify its own output.

---

## 11.4 Data Transformation

Every architectural layer follows the same processing model.

```text
Input
        │
        ▼
Validation
        │
        ▼
Processing
        │
        ▼
Output
```

Each transformation must be deterministic.

---

## 11.5 Data Integrity Principles

All architectural data follows these principles.

- Immutable after creation
- Explicit ownership
- Standardized structure
- No shared mutable state
- Forward-only data flow

These principles guarantee predictable execution across every architectural layer.

---

# 12. Dependency Rules

## 12.1 Overview

Dependency Rules define how architectural layers communicate throughout the RCBT system.

All dependencies follow a single downward direction.

Reverse dependencies and circular references are prohibited.

---

## 12.2 Dependency Model

### No Layer Skipping

```text
Application Layer
        │
        ▼
Infrastructure Layer
        │
        ▼
Discovery Layer
        │
        ▼
Runtime Layer
        │
        ▼
Workflow Layer
        │
        ▼
Report Layer
        │
        ▼
Export Layer
```

Each layer depends only on its immediate downstream layer through explicit Execution Context Objects.

---

## 12.3 Dependency Principles

### Downstream Communication

Dependencies always point downward.

---

### Explicit Contracts

Communication occurs only through standardized Execution Context Objects.

---

### No Circular Dependency

Circular dependencies between architectural layers are prohibited.

---

### Layer Isolation

Each layer owns its own implementation.

Internal implementation details must never be accessed directly.

---

### Stable Interfaces

Public contracts should remain stable even when implementation changes.

---

# 13. State Lifecycle

## 13.1 Overview

Every execution follows a predictable lifecycle from HAR import until export generation.

Each completed state becomes the prerequisite for the next state.

---

## 13.2 Lifecycle

```text
HAR Imported
        │
        ▼
Workspace Ready
        │
        ▼
HAR Parsed
        │
        ▼
Discovery Completed
        │
        ▼
Runtime Ready
        │
        ▼
Backup Running
        │
        ▼
Report Generated
        │
        ▼
Export Completed
        │
        ▼
Finished
```

Execution always progresses forward.

Rollback behavior is outside the scope of this architecture.

---

## 13.3 Lifecycle Principles

- Deterministic execution
- Explicit state ownership
- Sequential progression
- Context-driven transitions
- Reproducible execution

---

# 14. Error Boundaries

## 14.1 Overview

Every architectural layer owns its own failure boundary.

Errors should remain isolated within the originating layer whenever possible.

---

## 14.2 Error Boundary Model

```text
Workspace Error
        │
        ▼
Execution Stop

Parser Error
        │
        ▼
Execution Stop

Discovery Error
        │
        ▼
Execution Stop

Runtime Error
        │
        ▼
Retry or Abort

Workflow Error
        │
        ▼
Continue Reporting

Report Error
        │
        ▼
Continue Export

Export Error
        │
        ▼
Warning
```

---

## 14.3 Error Handling Principles

- Fail Fast
- Explicit Ownership
- Structured Reporting
- Layer Isolation
- Recoverability

---

# 15. Architectural Extension Points

## 15.1 Overview

The architecture has been designed to support future expansion without requiring major structural changes.

Future capabilities should integrate through existing architectural contracts whenever practical.

---

## 15.2 Planned Extensions

Potential future extensions include:

- Knowledge Engine
- Restore Runtime
- Plugin System
- Scheduler
- REST API Service
- Web Dashboard
- Parallel Execution
- Distributed Processing
- Cloud Synchronization

---

## 15.3 Extension Principles

Every future extension should:

- Preserve architectural consistency.
- Follow existing Execution Context Objects.
- Respect Dependency Rules.
- Maintain backward compatibility.
- Minimize impact on existing modules.

---

# 16. Architecture Maintenance Policy

ARCHITECTURE.md should be updated only when one or more of the following changes occur.

- Execution Flow changes.
- Repository Structure changes.
- System Architecture changes.
- Module Communication changes.
- Execution Context Objects change.
- Dependency Rules change.
- Architectural Contracts change.

Routine implementation changes should not require updates to this document.

---

# 17. Closing Statement

ARCHITECTURE.md defines the implementation architecture of the Ruijie Cloud Backup Toolkit.

It explains how architectural layers communicate, how information flows through the system, and how modules cooperate to produce deterministic execution.

Whenever architectural implementation changes, this document should be reviewed before implementation proceeds.

---

# End of ARCHITECTURE.md

## Document Metadata

| Item | Value |
|------|-------|
| Version | 3.0 |
| Status | Active |
| Classification | Technical Architecture |
| Maintained By | Project Owner & AI Engineering Partner |
| Source of Truth | Git Repository Source Code |

## Related Documents

- PROJECT_CONTEXT.md
- SESSION_CONTEXT.md
- API_DISCOVERY.md
- ROADMAP.md
- CHANGELOG.md
- CHAT_BOOTSTRAP.md
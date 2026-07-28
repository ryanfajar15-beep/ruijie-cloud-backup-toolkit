# Ruijie Cloud Backup Toolkit

## Project Information

| Item | Value |
|------|-------|
| Project | Ruijie Cloud Backup Toolkit |
| Version | 0.2.0-dev |
| Status | Active Development |
| Current Phase | Phase 3 - Request Discovery |

---

# Development Roadmap

## Phase 1 - Project Bootstrap
**Status:** ✅ Completed

### Objectives
- Initialize Git repository
- Create Python virtual environment
- Install dependencies
- Create project structure

### Deliverables
- Repository ready
- requirements.txt
- Folder structure

---

## Phase 2 - HAR Loader
**Status:** ✅ Completed

### Objectives
- Validate HAR file
- Load HAR
- Read entries

### Deliverables
- HAR successfully loaded
- Total entries detected: **326**

---

## Phase 3 - Request Discovery
**Status:** 🚧 In Progress

### Objectives
- Parse every HTTP request
- Detect API endpoints
- Group requests by method
- Extract URL path
- Extract query parameters
- Extract request headers

### Deliverables
- request_catalog.json

---

## Phase 4 - Authentication Extraction
**Status:** ⏳ Pending

### Objectives
- Extract Authorization
- Extract Cookie
- Extract CSRF Token
- Extract Tenant ID
- Extract Organization ID
- Extract User Information

### Deliverables
- auth.json

---

## Phase 5 - API Mapping
**Status:** ⏳ Pending

### Objectives
- Build API catalog
- Analyze request schema
- Analyze response schema
- Identify endpoint relationships

### Deliverables
- api_catalog.json

---

## Phase 6 - Backup Engine
**Status:** ⏳ Pending

### Objectives
- Download cloud resources
- Normalize data
- Save backup files

### Deliverables
- backup/

---

## Phase 7 - Restore Engine
**Status:** ⏳ Pending

### Objectives
- Restore configuration
- Validate dependencies
- Execute restore process

### Deliverables
- restore.py

---

## Phase 8 - Exporter
**Status:** ⏳ Pending

### Objectives
- Export JSON
- Export CSV
- Export Excel
- Export HTML

---

## Phase 9 - CLI
**Status:** ⏳ Pending

### Objectives
- analyze
- backup
- restore
- export

### Deliverables
- CLI Application

---

## Phase 10 - Release
**Status:** ⏳ Pending

### Target
- Version 1.0.0
- Documentation complete
- Production ready
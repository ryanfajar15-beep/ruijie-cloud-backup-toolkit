# Ruijie Cloud Backup Toolkit

## Architecture Overview

### Purpose

Ruijie Cloud Backup Toolkit adalah aplikasi Python yang bertujuan untuk:

- Menganalisis HAR hasil Ruijie Cloud
- Menemukan endpoint API
- Mengekstrak autentikasi
- Melakukan backup seluruh resource
- Melakukan restore konfigurasi
- Mengekspor hasil backup ke berbagai format

---

# High Level Workflow

```
HAR File
    │
    ▼
HAR Loader
    │
    ▼
Request Discovery
    │
    ▼
Authentication Extraction
    │
    ▼
API Mapping
    │
    ▼
Backup Engine
    │
    ▼
Exporter
    │
    ▼
Restore Engine
```

---

# Directory Structure

```
ruijie-cloud-backup/

src/
    parser/
    auth/
    discovery/
    backup/
    restore/
    exporter/
    models/
    utils/

docs/
tests/

input/
output/

backup.py
```

---

# Core Modules

## Parser

Tugas:

- membaca HAR
- validasi HAR
- membaca seluruh request

Output:

- parsed request

---

## Discovery

Tugas:

- mendeteksi endpoint API
- mengelompokkan endpoint
- menghitung request

Output:

- request_catalog.json

---

## Authentication

Tugas:

- Authorization
- Cookie
- CSRF
- Tenant
- User

Output:

- auth.json

---

## API Mapper

Tugas:

- membangun database endpoint
- mengetahui hubungan antar endpoint

Output:

- api_catalog.json

---

## Backup Engine

Tugas:

- mengambil seluruh data dari API
- menyimpan backup

Output:

backup/

---

## Restore Engine

Tugas:

- membaca backup
- restore ke cloud

---

## Exporter

Mendukung export:

- JSON
- CSV
- Excel
- HTML

---

# Design Principles

Project ini mengikuti prinsip:

- Modular
- Single Responsibility
- Reusable
- Testable
- Maintainable
- Logging First
- Type Hints
- Clean Architecture

---

# Version

Current Version

0.2.0-dev
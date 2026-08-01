# Phase 07 — Discovery Engine

Status

In Progress

---

## Objective

Phase ini bertujuan menyelesaikan seluruh proses reverse engineering
terhadap HAR sehingga seluruh knowledge yang dibutuhkan runtime dapat
diperoleh secara otomatis.

Setelah Phase ini selesai, runtime tidak lagi bergantung langsung
terhadap HAR.

---

## Scope

Authentication Discovery

RSA Discovery

Cookie Discovery

Redirect Discovery

Session Discovery

Endpoint Discovery

Workflow Discovery

Storage Discovery

Render Discovery

Export Discovery

Download Discovery

Response Schema Discovery

---

## Expected Output

analysis/

↓

Knowledge Engine

↓

Runtime

---

## Deliverables

- Endpoint Catalog
- Authentication Metadata
- Workflow Metadata
- Response Schema
- API Dependency
- Download Route
- Export Route
- Storage Route

---

## Out of Scope

Runtime Refactor.

Knowledge Engine.

Production Optimization.

Seluruh pekerjaan tersebut akan dikerjakan pada Phase berikutnya.

---

## Current Status

Not Started

---

## Notes

Seluruh proses discovery menggunakan tools reverse engineering
yang berada pada folder:

tools/

Output discovery disimpan pada:

analysis/

Runtime belum menggunakan hasil discovery secara langsung.

Knowledge Layer akan dibangun setelah discovery selesai.
# RCBT CHAT BOOTSTRAP

# Ruijie Cloud Backup Toolkit (RCBT)

## Purpose

File ini adalah entry point ketika melanjutkan project RCBT dari chat baru.

Fungsi utama:

- memberikan startup context
- mendefinisikan AI working rules
- menetapkan source of truth
- menentukan context reading order
- menjaga konsistensi engineering

---

# AI Working Rules

These rules have higher priority than implementation convenience.
Whenever implementation conflicts with these rules, the conflict must be explained before proceeding.

AI wajib mengikuti aturan berikut selama pengembangan RCBT.

## Engineering Rules

- Jangan mengubah arsitektur tanpa persetujuan.
- Jangan mengubah workflow project tanpa diskusi.
- Jangan rename module tanpa persetujuan.
- Jangan membuat duplicate module.
- Selalu menjaga backward compatibility.
- Semua implementasi harus production-ready.
- Selalu mengikuti roadmap yang sedang aktif.
- Jangan membuat keputusan arsitektur berdasarkan asumsi.

## Implementation Rules

- Jangan meminta user mencari line tertentu.
- Jangan meminta edit manual jika file dapat dikirim penuh.
- Jika file berubah, kirim file lengkap.
- Jika file terlalu panjang gunakan format:
  - Part 1/x
  - Part 2/x
  - Part 3/x
- Setiap part harus dapat langsung di-copy-paste.
- Jangan memotong kode.
- Jangan menghilangkan import.
- Jangan menghilangkan comment penting.
- Gunakan Python automation jika memungkinkan.
- Jangan melakukan hardcode path maupun konfigurasi.

## Reverse Engineering Rules

- Jangan membuat asumsi endpoint.
- Jangan membuat asumsi payload.
- Jangan membuat asumsi authentication.
- Gunakan hasil reverse engineering HAR sebagai acuan.
- Runtime tidak boleh dibangun berdasarkan dugaan.

---

# Project Identity

Project

Ruijie Cloud Backup Toolkit (RCBT)

Type

Production-grade automation toolkit

Tujuan

RCBT dibuat untuk:

- membaca export HAR
- melakukan API discovery
- memahami workflow internal Ruijie Cloud
- mengelola authentication
- menjalankan backup automation
- menghasilkan report

---

# Source of Truth

Repository adalah sumber utama project.

Chat history bukan sumber permanen.

Context project disimpan melalui:

docs/

Structure:

docs/

├── CHAT_BOOTSTRAP.md
├── SESSION_CONTEXT.md
├── PROJECT_CONTEXT.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── CHANGELOG.md
├── ENGINEERING_MEMORY_GUIDE.md
├── ENGINEERING_MEMORY.md
├── TODO.md
├── HISTORY/
├── DECISIONS/
└── TROUBLESHOOTING/

Source Priority

Project Documentation refers to the engineering documentation maintained under `docs/`.

Jika terjadi perbedaan antara repository dengan chat, repository menjadi acuan utama.

---

# Context Reading Order

Required

1. CHAT_BOOTSTRAP.md
2. SESSION_CONTEXT.md
3. PROJECT_CONTEXT.md
4. ARCHITECTURE.md
5. ROADMAP.md
6. TODO.md
7. CHANGELOG.md

Optional (Engineering Knowledge)

- ENGINEERING_MEMORY_GUIDE.md
- ENGINEERING_MEMORY.md
- HISTORY/
- DECISIONS/
- TROUBLESHOOTING/

Melanjutkan project dari kondisi terakhir tanpa mengulang investigasi maupun keputusan engineering yang telah selesai.

---

Task Resolution Rule
--------------------

AI must determine the current engineering task exclusively from docs/TODO.md.

SESSION_CONTEXT.md provides project summary only.

If a conflict exists between SESSION_CONTEXT.md and TODO.md, TODO.md is authoritative for active engineering tasks.

AI must always continue from the first unchecked checklist item in TODO.md unless explicitly instructed otherwise.

---

Bootstrap Principle
-------------------

CHAT_BOOTSTRAP.md defines startup rules only.

It intentionally does not duplicate engineering workflow, project architecture, roadmap, or implementation details.

Those responsibilities belong to:

- `PROJECT_CONTEXT.md`
- `ARCHITECTURE.md`
- `AI_WORKFLOW.md`
- `SESSION_CONTEXT.md`
- `TODO.md`

---

# Core Architecture

Workflow utama

incoming/

↓

backup.py

↓

Workspace

↓

HAR Importer

↓

HAR Parser

↓

Discovery Engine

↓

Runtime Layer

↓

Backup Workflow

↓

Report Layer

↓

Export Layer

---

# Main Controller Rule

backup.py adalah Main Controller.

Tanggung jawab:

- menjalankan workflow
- menghubungkan seluruh module
- mengatur lifecycle project

backup.py tidak boleh:

- parsing HAR
- authentication logic
- API implementation detail
- download logic
- report generation logic
- business logic

---

# Module Responsibility

## Parser

Bertanggung jawab:

- membaca data
- normalisasi data
- ekstraksi informasi

Tidak melakukan:

- login
- API request
- backup execution

---

## Workspace

Bertanggung jawab:

- project workspace
- path management
- metadata project

Tidak melakukan:

- parsing
- authentication
- backup

---

## Authentication

Bertanggung jawab:

- credential management
- login workflow
- session lifecycle
- authentication validation
- session persistence

Tidak melakukan:

- HAR parsing
- backup execution
- business workflow
- report generation

---

## API Client

Bertanggung jawab:

- komunikasi HTTP/API
- request handling
- response handling
- API error handling
- endpoint execution

Tidak melakukan:

- authentication decision
- business workflow
- backup orchestration
- HAR parsing

---

## Backup

Bertanggung jawab:

- menjalankan backup workflow
- menggunakan API Client
- mengelola proses download
- menyimpan hasil backup
- mengelola output backup

Tidak melakukan:

- membaca HAR langsung
- authentication
- endpoint discovery
- business configuration

---

# Phase Lifecycle Management

## Phase Structure

RCBT menggunakan struktur phase yang konsisten.

Major Phase

Phase X

Sub Phase

Phase X.Y

Contoh

Phase 6

↓

Phase 6.0 Runtime Foundation

↓

Phase 6.1 Credential Management

↓

Phase 6.2 Authentication Runtime

↓

Phase 6.3 API Client Foundation

↓

Phase 6.4 Workflow Foundation

↓

Phase 6.5 Runtime Stabilization

↓

Phase 6 Completed

Phase 7

↓

Phase 7.0 Discovery Finalization

↓

Phase 7.1 Knowledge Engine

↓

Phase 7.2 Runtime Integration

↓

Phase 7.3 Production Optimization

---

# Phase Status Definition

Setiap phase wajib memiliki salah satu status berikut.

## PLANNING

Phase belum dimulai.

## IN PROGRESS

Phase sedang dikerjakan.

## BLOCKED

Phase tidak dapat dilanjutkan karena dependency, bug, atau keputusan engineering.

## REVIEW

Seluruh implementasi selesai dan sedang dilakukan review.

## COMPLETED

Phase selesai, telah diuji, terdokumentasi, dan siap dilanjutkan ke phase berikutnya.

---

# Current Phase Rule

SESSION_CONTEXT.md is the authoritative source for:

- Current Phase
- Current Milestone
- Repository Metadata

Active engineering tasks are maintained exclusively in:

docs/TODO.md

---

# Moving Phase Rule

Tidak diperbolehkan memulai Phase berikutnya sebelum seluruh checklist berikut terpenuhi.

Checklist

[ ] Semua Sub Phase selesai.

[ ] Testing selesai.

[ ] Validation selesai.

[ ] Error penting telah didokumentasikan.

[ ] Technical Decision telah dicatat.

[ ] HISTORY Phase telah dibuat.

[ ] CHANGELOG telah diperbarui.

[ ] ROADMAP telah diperbarui.

[ ] SESSION_CONTEXT.md telah diperbarui.

[ ] TODO telah diperbarui.

---

# Phase Documentation Output

Setiap Phase yang selesai wajib menghasilkan dokumentasi.

## History Document

Lokasi

docs/HISTORY/

Format

PHASE_<NUMBER>_<NAME>.md

Minimal berisi:

- Overview
- Objective
- Scope
- Implementation
- Investigation
- Error History
- Solution
- Technical Decision
- Architecture Impact
- Testing Result
- Deliverables
- Lessons Learned
- Next Phase

---

# Architecture Decision Record (ADR)

Seluruh keputusan engineering yang memengaruhi project wajib didokumentasikan.

Lokasi

docs/DECISIONS/

Format

ADR_<NUMBER>_<NAME>.md

Template

## Problem

Masalah yang membutuhkan keputusan.

## Context

Kondisi ketika keputusan dibuat.

## Options Considered

Seluruh alternatif yang dianalisis.

## Decision

Keputusan final.

## Reason

Alasan memilih keputusan.

## Consequences

Konsekuensi jangka pendek dan jangka panjang.

## Impact

Dampak terhadap:

- Architecture
- Module
- Workflow
- Maintainability
- Scalability
- Backward Compatibility

---

# Engineering Implementation Principles

Seluruh implementasi harus mengikuti prinsip berikut.

- Single Responsibility Principle (SRP)
- Separation of Concerns (SoC)
- Backward Compatibility
- Modular Design
- Reusability
- Maintainability
- Scalability
- Production Readiness

Jika terdapat konflik antara implementasi dengan prinsip di atas.

AI wajib menjelaskan alasan teknis sebelum melakukan perubahan.


---

# Troubleshooting Documentation

Seluruh error penting wajib didokumentasikan.

Lokasi

docs/TROUBLESHOOTING/

Format

PHASE_<NUMBER>_ERRORS.md

Minimal berisi:

## Error

Pesan error atau gejala yang muncul.

## Investigation

Langkah investigasi yang dilakukan.

## Root Cause

Penyebab utama.

## Solution

Solusi yang diterapkan.

## Validation

Cara memastikan solusi berhasil.

## Prevention

Cara mencegah masalah yang sama terjadi kembali.

## Reference

Referensi commit, phase, atau ADR jika ada.

---

# Engineering Memory Rule

Selama development berlangsung.

Seluruh informasi penting harus dianggap sebagai Engineering Knowledge.

Yang wajib dicatat:

- Error yang muncul.
- Command troubleshooting.
- Hasil investigasi.
- Keputusan teknis.
- Alternatif solusi.
- Solusi yang ditolak.
- Perubahan architecture.
- Perubahan workflow.
- Perubahan dependency.
- Technical debt.
- Known issue.
- Kesepakatan development.

Tujuan

Agar AI maupun engineer lain dapat memahami alasan di balik setiap keputusan tanpa mengulang investigasi.

---

# AI Continuation Rule

Saat melanjutkan project RCBT.

AI wajib:

- Membaca seluruh required context terlebih dahulu.
- Membaca engineering knowledge bila diperlukan.
- Memahami Current Phase.
- Memahami Current Milestone.
- Determine the active engineering task from docs/TODO.md.
- Memahami arsitektur project.
- Mengikuti seluruh keputusan engineering sebelumnya.
- Menjaga backward compatibility.
- Tidak mengulang investigasi yang telah selesai.
- Tidak mengulang implementasi yang telah selesai.
- Tidak mengubah workflow tanpa persetujuan.

Jika terdapat konflik antara repository dengan chat.

Repository menjadi acuan utama.

---

# AI Quality Standard

Sebelum memberikan implementasi.

AI wajib memastikan:

- Selaras dengan arsitektur project.
- Mengikuti ROADMAP.
- Mengikuti SESSION_CONTEXT.
- Mengikuti TODO.md sebagai Engineering Task Tracker.
- Mengikuti keputusan pada DECISIONS.
- Tidak membuat asumsi.
- Tidak menghasilkan duplicate module.
- Tidak merusak backward compatibility.
- Siap digunakan pada production.

Jika salah satu poin di atas tidak dapat dipenuhi.

AI wajib menjelaskan alasannya terlebih dahulu sebelum memberikan implementasi.

---

# Chat Transfer Protocol

Ketika berpindah chat.

AI tidak boleh meminta user menjelaskan ulang history project.

AI harus menggunakan dokumentasi project sebagai sumber utama.

## Required

docs/CHAT_BOOTSTRAP.md

docs/SESSION_CONTEXT.md

docs/PROJECT_CONTEXT.md

docs/TODO.md

## Recommended

docs/ARCHITECTURE.md

docs/ROADMAP.md

docs/CHANGELOG.md

## Optional (Engineering Knowledge)

docs/ENGINEERING_MEMORY_GUIDE.md

docs/ENGINEERING_MEMORY.md

docs/HISTORY/

docs/DECISIONS/

docs/TROUBLESHOOTING/

Dengan dokumen tersebut AI harus dapat melanjutkan project tanpa mengulang investigasi.

---

# New Chat Startup Rule

Saat memulai chat baru.

AI wajib memahami urutan berikut.

1. Project Identity

2. Engineering Rules

3. Existing Architecture

4. Current Phase

5. Current Milestone

6. Engineering Task Tracker

7. Previous Decisions

8. AI Workflow

9. Roadmap

10. Current Repository State

## Sumber Informasi

| Document | Purpose |
|----------|---------|
| CHAT_BOOTSTRAP.md | AI startup contract dan startup rules. |
| SESSION_CONTEXT.md | Current project snapshot. |
| PROJECT_CONTEXT.md | Engineering constitution dan long-term project context. |
| ARCHITECTURE.md | Technical architecture dan module responsibilities. |
| ROADMAP.md | Long-term development roadmap. |
| TODO.md | Engineering Task Tracker (Single Source of Truth untuk active engineering tasks). |
| AI_WORKFLOW.md | Engineering workflow and lifecycle. |
| CHANGELOG.md | Completed engineering milestones. |
| HISTORY/ | Historical engineering summary per phase. |
| DECISIONS/ | Architecture Decision Records (ADR). |
| Repository Source Code | Actual implementation (Primary Source of Truth). |

## Source Priority

Jika terjadi konflik, gunakan prioritas berikut:

1. Repository Source Code
2. SESSION_CONTEXT.md
3. TODO.md
4. PROJECT_CONTEXT.md
5. ARCHITECTURE.md
6. ROADMAP.md
7. CHANGELOG.md
8. AI_WORKFLOW.md
9. HISTORY/
10. DECISIONS/
11. Chat Conversation

Repository Source Code selalu menjadi Primary Source of Truth.

---

# RCBT Engineering Principles

Seluruh pengembangan RCBT harus mengikuti prinsip berikut.

1. Clean Architecture

2. Single Responsibility Principle (SRP)

3. Separation of Concerns (SoC)

4. Modular Design

5. Maintainability

6. Scalability

7. Backward Compatibility

8. Reproducible Development

9. Production Readiness

10. Complete Engineering Documentation

Seluruh keputusan engineering harus mempertimbangkan prinsip-prinsip di atas.

---

# Final Rule

Jangan melakukan perubahan hanya karena terlihat lebih mudah.

Setiap perubahan wajib mempertimbangkan:

- Architecture Impact
- Workflow Impact
- Module Responsibility
- Maintenance Impact
- Future Scalability
- Backward Compatibility
- Production Readiness

Jika terdapat trade-off.

AI wajib menjelaskan:

- alasan teknis.
- keuntungan.
- risiko.
- dampak jangka panjang.

Sebelum melakukan implementasi.

---

# AI Confidence Rule

AI tidak boleh menyatakan sesuatu sebagai fakta apabila tidak didukung oleh:

- Repository Source Code.
- SESSION_CONTEXT.md
- Dokumentasi Project.
- Hasil Reverse Engineering.
- Output Runtime.
- Hasil Testing.

Jika informasi belum dapat dipastikan.

AI wajib menggunakan salah satu pernyataan berikut:

- Berdasarkan repository saat ini...
- Berdasarkan hasil reverse engineering...
- Berdasarkan dokumentasi...
- Ini merupakan asumsi dan perlu divalidasi.

AI tidak boleh menyajikan asumsi sebagai fakta.

---
# AI Mission

AI berperan sebagai Engineering Partner.

Bukan hanya menghasilkan kode.

Tetapi juga menjaga:

- konsistensi arsitektur.
- kualitas implementasi.
- kualitas dokumentasi.
- kualitas engineering decision.
- kualitas reverse engineering.
- maintainability.
- scalability.
- keberlanjutan project.

Prioritas utama AI adalah menjaga kualitas repository jangka panjang.

AI harus lebih mengutamakan konsistensi project dibanding menghasilkan implementasi yang cepat.

---

# Bootstrap Completion

Jika seluruh dokumen telah dipahami.

AI tidak perlu meminta user mengulang konteks project.

AI langsung:

- Memahami Current Phase dari SESSION_CONTEXT.md.
- Continue from the first unchecked checklist item in docs/TODO.md.
- mengikuti seluruh Engineering Rules.
- menjaga konsistensi arsitektur.
- menjaga kualitas dokumentasi.
- menghindari duplicate implementation.
- menjaga backward compatibility.

Tujuan utama AI adalah menjadi engineering partner yang konsisten terhadap repository, dokumentasi, roadmap, dan keputusan project yang telah disepakati.

Jika informasi yang diperlukan belum tersedia pada dokumentasi maupun repository, AI wajib meminta informasi tambahan sebelum membuat keputusan implementasi.

# End Of CHAT_BOOTSTRAP

Dokumen ini merupakan kontrak kerja antara User dan AI selama pengembangan Ruijie Cloud Backup Toolkit (RCBT).

Seluruh implementasi harus mengikuti aturan, arsitektur, workflow, roadmap, dan engineering principles yang tercantum pada dokumen ini.

Jika terdapat konflik antara percakapan dengan repository.

Repository Source Code merupakan source of truth utama.

Dokumentasi project menjadi referensi engineering yang menjelaskan alasan, keputusan, workflow, dan status project.

Apabila terjadi konflik, Repository Source Code menjadi acuan utama.
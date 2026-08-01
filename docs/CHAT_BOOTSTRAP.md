# RCBT CHAT BOOTSTRAP

# Ruijie Cloud Backup Toolkit (RCBT)

## Purpose

File ini adalah entry point ketika melanjutkan project RCBT dari chat baru.

Fungsi utama:

- memberikan pemahaman project
- menjaga architecture consistency
- menjelaskan development workflow
- menjelaskan aturan implementasi
- menjaga dokumentasi engineering

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

## Git Workflow Rules

- Jangan membuat commit sebelum phase selesai.
- Ikuti Git workflow project.
- Update CHANGELOG setiap phase selesai.
- Update ROADMAP jika phase berubah.
- Update SESSION_CONTEXT jika berpindah milestone.

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
├── TODO.md
├── HISTORY/
├── DECISIONS/
└── TROUBLESHOOTING/

Source Priority

1. Repository Source Code
2. SESSION_CONTEXT.md
3. Project Documentation
4. History & Decisions
5. Chat Conversation

Jika terjadi perbedaan antara repository dengan chat, repository menjadi acuan utama.

---

# Context Reading Order

Saat membuka chat baru AI wajib membaca dokumen dengan urutan berikut:

1.

docs/CHAT_BOOTSTRAP.md

2.

docs/SESSION_CONTEXT.md

3.

docs/PROJECT_CONTEXT.md

4.

docs/ARCHITECTURE.md

5.

docs/ROADMAP.md

6.

docs/TODO.md

7.

docs/CHANGELOG.md

8.

docs/HISTORY/

9.

docs/DECISIONS/

10.

docs/TROUBLESHOOTING/

Tujuan

Melanjutkan project dari kondisi terakhir tanpa mengulang investigasi maupun keputusan engineering yang telah selesai.

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

Status project tidak ditentukan dari CHAT_BOOTSTRAP.md.

Sumber utama status project adalah:

docs/SESSION_CONTEXT.md

SESSION_CONTEXT.md wajib menjadi referensi utama untuk:

- Current Phase
- Current Sub Phase
- Current Milestone
- Current Task
- Completed Task
- Blocker
- Next Action
- Current Git Branch
- Last Commit

Jika terdapat perbedaan antara CHAT_BOOTSTRAP.md dan SESSION_CONTEXT.md, maka SESSION_CONTEXT.md menjadi acuan utama.

---

# Phase Completion Rule

Major Phase tidak boleh dinyatakan selesai apabila masih terdapat Sub Phase yang belum selesai.

Sebuah Phase hanya dapat berubah menjadi COMPLETED apabila memenuhi seluruh syarat berikut:

- Semua Sub Phase selesai.
- Seluruh implementasi telah selesai.
- Testing berhasil.
- Tidak ada blocker kritis.
- Dokumentasi telah diperbarui.
- CHANGELOG telah diperbarui.
- SESSION_CONTEXT.md telah diperbarui.
- HISTORY Phase telah dibuat.
- Seluruh perubahan telah di-review.

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

# Development Workflow

Seluruh implementasi wajib mengikuti workflow berikut.

Analysis

↓

Design

↓

Architecture Decision

↓

Implementation

↓

Validation

↓

Testing

↓

Documentation

↓

Git Commit

Tidak diperbolehkan melakukan Git Commit sebelum seluruh tahapan di atas selesai.

---

# Testing Rule

Setiap implementasi wajib memiliki langkah testing yang jelas.

Minimal terdiri dari:

- Run Command
- Validation Command
- Expected Result

Jika implementasi belum dapat diuji.

AI wajib menjelaskan alasannya.

---

# Repository Response Rule

Jika perubahan tidak menyentuh repository.

Berikan:

- Analisis.
- Penjelasan.
- Rekomendasi.
- Keputusan teknis.

Jika perubahan menyentuh repository.

AI wajib memberikan:

- Kirim file lengkap.
- Berikan executable command.
- Berikan validation command.
- Berikan run command.
- Berikan Git command (jika Phase telah selesai).

AI tidak boleh:

- Meminta user mencari line number.
- Meminta user mencari posisi kode.
- Meminta edit manual.
- Memberikan patch yang tidak lengkap.
- Memberikan potongan kode yang tidak dapat langsung digunakan.

Jika file terlalu panjang.

AI wajib menggunakan format:

Part 1/x

Part 2/x

Part 3/x

Setiap Part harus dapat langsung di-copy-paste.

---

# Response Format Rule

Setiap implementasi repository wajib menggunakan format berikut.

📌 Phase X.X

Action
(Create / Update / Replace)

Update File

<path file>

<isi file lengkap atau Part x/x>

Run

<command>

Validation

<command>

Commit

<hanya jika Phase telah selesai>

---

# Repository Modification Strategy

Seluruh perubahan repository harus mengikuti prioritas berikut.

Priority

1. Python Automation
2. Python Replacement
3. Full File Generator
4. Heredoc
5. Manual Edit (hanya jika benar-benar diperlukan)

Hindari:

- nano untuk file panjang.
- edit manual pada file repository.
- mencari line number.
- mencari posisi block secara manual.
- copy-paste ke tengah file.
- patch yang tidak dapat langsung digunakan.

Tujuan:

- reproducible
- mengurangi human error
- menjaga konsistensi
- mempermudah automation
- mempermudah rollback

---

# Long File Rule

Jika file terlalu panjang.

AI wajib menggunakan format berikut.

Part 1/x

Part 2/x

Part 3/x

dst.

Setiap Part wajib:

- memiliki urutan yang jelas.
- dapat langsung di-copy-paste.
- tidak membutuhkan edit manual.
- tidak menghilangkan import.
- tidak menghilangkan comment penting.
- tidak memotong function atau class.

Jika memungkinkan.

AI lebih memilih mengirim file penuh dibanding patch.

---

# Documentation Rule

Dokumentasi merupakan bagian dari development lifecycle.

Dokumentasi tidak boleh dianggap sebagai pekerjaan setelah coding selesai.

Setiap perubahan architecture, workflow, ataupun engineering decision wajib diikuti pembaruan dokumentasi yang relevan.

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

# Documentation Update Rule

AI wajib memperbarui dokumentasi sesuai perubahan project.

Perubahan yang wajib diikuti update dokumentasi:

- Phase berubah.
- Architecture berubah.
- Workflow berubah.
- Folder Structure berubah.
- Engineering Decision baru.
- Technical Debt baru.
- Known Issue baru.
- Milestone selesai.

Minimal dokumen yang harus diperbarui sesuai kebutuhan:

- ROADMAP.md
- CHANGELOG.md
- TODO.md
- SESSION_CONTEXT.md
- HISTORY/*
- DECISIONS/*
- TROUBLESHOOTING/*

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

- Membaca seluruh context terlebih dahulu.
- Memahami Current Phase.
- Memahami Current Milestone.
- Memahami Current Task.
- Memahami arsitektur project.
- Mengikuti seluruh keputusan engineering sebelumnya.
- Menjaga backward compatibility.
- Tidak mengulang investigasi yang telah selesai.
- Tidak mengulang implementasi yang telah selesai.
- Tidak mengubah workflow tanpa persetujuan.

Jika terdapat konflik antara repository dengan chat.

Repository menjadi acuan utama.

---

# AI Response Rule

Jika hanya membutuhkan diskusi.

Berikan:

- Analisis.
- Pertimbangan.
- Risiko.
- Trade-off.
- Rekomendasi.

Jika membutuhkan perubahan repository.

AI wajib memberikan:

📌 Phase

Action

Create / Update / Replace

Update File

<path>

<file lengkap atau Part x/x>

Run

<command>

Validation

<command>

Commit

<hanya jika Phase telah selesai>

AI tidak boleh memberikan potongan kode yang mengharuskan user mencari lokasi secara manual.

---

# Response Priority

Urutan prioritas jawaban.

1. Executable Command
2. Full File / Part x/x
3. Validation Command
4. Git Workflow
5. Technical Explanation

Penjelasan diberikan apabila:

- terdapat keputusan arsitektur.
- terdapat trade-off.
- terdapat risiko teknis.
- terdapat perubahan workflow.
- terdapat perubahan engineering decision.

Hindari penjelasan panjang apabila tidak diminta secara eksplisit.

---

# AI Quality Standard

Sebelum memberikan implementasi.

AI wajib memastikan:

- Selaras dengan arsitektur project.
- Mengikuti ROADMAP.
- Mengikuti SESSION_CONTEXT.
- Mengikuti keputusan pada DECISIONS.
- Tidak membuat asumsi.
- Tidak menghasilkan duplicate module.
- Tidak merusak backward compatibility.
- Siap digunakan pada production.

Jika salah satu poin di atas tidak dapat dipenuhi.

AI wajib menjelaskan alasannya terlebih dahulu sebelum memberikan implementasi.

---

# Reproducible Change Rule

Seluruh perubahan repository harus dapat direproduksi dari terminal.

Prioritas implementasi:

1. Python Automation
2. Python Replacement
3. Full File Generator
4. Heredoc
5. Manual Edit (opsi terakhir)

Contoh

Create File

Python Generator

Update File

Python Replacement

Replace File

Full File Generator

Large File

Part 1/x

Part 2/x

Part 3/x

Validation

Explicit Validation Command

AI harus menghindari perubahan yang tidak dapat direproduksi.

---

# Git Workflow Rule

Seluruh milestone development wajib mengikuti Git workflow.

Workflow

1. Review perubahan

git status

2. Stage

git add <file>

atau

git add .

3. Commit

git commit -m "<message>"

4. Push

git push

AI tidak boleh meminta commit apabila:

- Phase belum selesai.
- Testing belum selesai.
- Validation belum selesai.
- Dokumentasi belum diperbarui.

---

# Repository Metadata Rule

Setiap selesai milestone atau phase.

AI wajib memperbarui metadata repository pada:

docs/SESSION_CONTEXT.md

Field yang wajib diperbarui:

- Repository Branch
- Git HEAD
- Last Commit
- Last Update

Contoh

Repository Branch

main

Git HEAD

7970ee6

Last Commit

docs(roadmap): close phase 6 and start phase 7

Last Update

2026-08-01

Metadata repository harus selalu sinkron dengan kondisi repository aktual.

---

# Documentation Synchronization Rule

Sebelum Git Commit.

AI wajib memastikan dokumentasi telah sinkron.

Minimal:

- SESSION_CONTEXT.md
- ROADMAP.md
- CHANGELOG.md
- TODO.md

Jika Phase selesai.

AI juga wajib:

- membuat HISTORY phase.
- memperbarui Git Metadata.
- memperbarui Current Phase.
- memperbarui Current Task.
- memperbarui Next Milestone.

Dokumentasi harus selesai sebelum Git Commit dilakukan.

---

# Commit Principle

Setiap commit harus:

- menjelaskan tujuan perubahan.
- menggunakan Conventional Commit.
- menggambarkan perubahan secara ringkas.
- konsisten dengan phase aktif.

Contoh

feat(auth): implement login service

fix(session): resolve cookie persistence

refactor(api): extract render client

docs(phase): close phase 6

docs(roadmap): start phase 7

test(authentication): validate login workflow

Commit besar yang mencampur banyak pekerjaan harus dihindari.

---

# Chat Transfer Protocol

Ketika berpindah chat.

AI tidak boleh meminta user menjelaskan ulang history project.

AI harus menggunakan dokumentasi project sebagai sumber utama.

Minimal dokumen yang diunggah:

docs/CHAT_BOOTSTRAP.md

docs/SESSION_CONTEXT.md

Jika diperlukan.

Tambahkan:

docs/PROJECT_CONTEXT.md

docs/ARCHITECTURE.md

docs/ROADMAP.md

History Phase terakhir.

Decision terakhir (jika ada).

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

6. Active Task

7. Previous Decisions

8. Development Workflow

9. Roadmap

10. Current Repository State

Sumber informasi

CHAT_BOOTSTRAP.md

Aturan kerja AI.

SESSION_CONTEXT.md

Status project saat ini.

PROJECT_CONTEXT.md

Gambaran project.

ARCHITECTURE.md

Arsitektur project.

ROADMAP.md

Target pengembangan.

CHANGELOG.md

Riwayat perubahan.

HISTORY/

Ringkasan setiap phase.

DECISIONS/

Keputusan engineering.

Repository Source Code

Implementasi aktual.

Jika terjadi konflik.

Prioritas acuan adalah:

1. Repository Source Code

2. SESSION_CONTEXT.md

3. PROJECT_CONTEXT.md

4. ARCHITECTURE.md

5. ROADMAP.md

6. HISTORY

7. Chat Conversation

Repository selalu menjadi source of truth.

---

# Phase Completion Final Checklist

Sebelum suatu Phase dinyatakan COMPLETED.

Seluruh checklist berikut wajib terpenuhi.

## Development

[ ] Objective tercapai.

[ ] Scope Phase selesai.

[ ] Seluruh implementasi selesai.

[ ] Validation berhasil.

[ ] Testing berhasil.

[ ] Tidak ada unresolved blocker.

---

## Investigation

[ ] Seluruh investigasi terdokumentasi.

[ ] Error penting telah dicatat.

[ ] Root Cause telah ditemukan.

[ ] Solution telah didokumentasikan.

[ ] Lessons Learned telah dicatat.

---

## Documentation

[ ] HISTORY document dibuat.

[ ] ADR / DECISION document dibuat jika diperlukan.

[ ] TROUBLESHOOTING document dibuat jika diperlukan.

[ ] CHANGELOG.md diperbarui.

[ ] ROADMAP.md diperbarui.

[ ] TODO.md diperbarui.

---

## Context

[ ] SESSION_CONTEXT.md diperbarui.

[ ] PROJECT_CONTEXT.md diperbarui jika diperlukan.

[ ] CHAT_BOOTSTRAP.md diperbarui apabila terdapat perubahan workflow atau engineering rules.

---

## Git

[ ] Git HEAD diperbarui.

[ ] Last Commit diperbarui.

[ ] Last Update diperbarui.

[ ] git status bersih.

[ ] Commit dibuat.

[ ] Push berhasil.

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

- melanjutkan Current Phase.
- melanjutkan Active Task.
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
# ==============================================================================
# RUIJIE CLOUD BACKUP TOOLKIT (RCBT)
# DEVELOPMENT CONTRACT
# ==============================================================================

| Property | Value |
|----------|-------|
| Document | Development Contract |
| Project | Ruijie Cloud Backup Toolkit (RCBT) |
| Version | 1.0 |
| Status | Frozen |
| Maintainer | Project Owner & AI Development Partner |
| Scope | Entire RCBT Project |

---

# DOCUMENT PURPOSE

Dokumen ini merupakan standar kerja resmi seluruh AI yang terlibat
dalam pengembangan Ruijie Cloud Backup Toolkit (RCBT).

Dokumen ini mendefinisikan cara AI:

- berpikir
- mengambil keputusan
- melakukan implementasi
- melakukan review
- menghasilkan source code
- berkomunikasi selama development

Seluruh AI wajib mengikuti aturan dalam dokumen ini selama tidak
bertentangan dengan kebijakan platform.

Apabila terdapat konflik antara chat, asumsi AI, dan source code,
maka source code project selalu menjadi referensi utama.

---

# REVISION HISTORY

| Version | Date | Description |
|----------|------------|------------------------------|
| 1.0 | 2026-07-30 | Initial Development Contract |

---

# TABLE OF CONTENTS

- Document Information
- Document Purpose
- Revision History
- Table of Contents
- Document Conventions
- Document Maintenance Rule
- Engineering Principles

- Chapter 1 — Identity & Purpose
- Chapter 2 — Working Rules
- Chapter 3 — Response Rules
- Chapter 4 — File & Folder Rules
- Chapter 5 — Coding Standards
- Chapter 6 — Git Workflow
- Chapter 7 — Error Handling & Logging
- Chapter 8 — Architecture & Phase Rules
- Chapter 9 — Communication Rules
- Chapter 10 — Definition of Done

- Appendix A — Good Response Examples
- Appendix B — Bad Response Examples
- Appendix C — Common Mistakes
- Appendix D — Command Templates


---

# DOCUMENT CONVENTIONS

Dokumen ini menggunakan konvensi berikut.

## Keywords

Kata-kata berikut mempunyai arti khusus.

| Keyword | Meaning |
|----------|---------|
| MUST | Wajib dilakukan. Tidak boleh diabaikan. |
| MUST NOT | Dilarang dilakukan. |
| SHOULD | Sangat disarankan. Boleh berbeda jika memiliki alasan yang kuat. |
| MAY | Bersifat opsional. |

---

## Terminology

| Term | Description |
|------|-------------|
| AI | Seluruh Artificial Intelligence yang membantu development project RCBT. |
| User | Project Owner atau Developer yang mengelola project RCBT. |
| Project | Ruijie Cloud Backup Toolkit (RCBT). |
| Module | Sebuah komponen Python yang memiliki satu tanggung jawab (Single Responsibility). |
| Source Code | Seluruh kode yang berada di dalam repository project. |
| Documentation | Seluruh dokumen pada folder `docs/`. |

---

## Document Structure

Dokumen ini disusun menggunakan struktur berikut.

Document

↓

Chapter

↓

Section

↓

Rule

Contoh:

Chapter 4

↓

4.2

↓

4.2.3

---

## Rule Priority

Jika terdapat dua aturan yang saling bertentangan,
prioritasnya adalah:

1. Platform Policy
2. Source Code Project
3. DEVELOPMENT_CONTRACT.md
4. CHAT_BOOTSTRAP.md
5. PROJECT_CONTEXT.md
6. ARCHITECTURE.md
7. ROADMAP.md
8. SESSION_CONTEXT.md
9. HISTORY
10. Chat Session

---

## Language

Dokumen ini menggunakan:

- Bahasa Indonesia sebagai bahasa utama.
- Istilah teknis menggunakan Bahasa Inggris.
- Nama class, function, module, package, dan variable tetap menggunakan Bahasa Inggris.

---

## Naming Convention

Penamaan mengikuti standar berikut.

| Object | Convention |
|---------|------------|
| Folder | snake_case |
| File | snake_case |
| Module | snake_case |
| Class | PascalCase |
| Function | snake_case |
| Variable | snake_case |
| Constant | UPPER_CASE |

---

## Reading Order

AI WAJIB membaca dokumen sesuai urutan berikut.

1. DEVELOPMENT_CONTRACT.md
2. Chapter yang relevan.
3. CHAT_BOOTSTRAP.md
4. PROJECT_CONTEXT.md
5. ARCHITECTURE.md
6. ROADMAP.md
7. SESSION_CONTEXT.md
8. HISTORY yang relevan.
9. Source Code yang akan diubah.

AI dilarang memberikan analisis, review, maupun implementasi
sebelum konteks yang relevan selesai dipelajari.

---

# DOCUMENT MAINTENANCE RULE

Development Contract merupakan **Single Source of Truth**
untuk seluruh standar kerja AI pada project RCBT.

Seluruh AI wajib mengacu pada dokumen ini sebelum melakukan:

- analisis
- review
- implementasi
- refactoring
- testing
- dokumentasi

---

## Source of Truth

Seluruh AI wajib menggunakan urutan referensi berikut
dalam setiap sesi development.

1. Source Code Project
2. DEVELOPMENT_CONTRACT.md
3. CHAT_BOOTSTRAP.md
4. PROJECT_CONTEXT.md
5. ARCHITECTURE.md
6. ROADMAP.md
7. SESSION_CONTEXT.md
8. HISTORY
9. Chat Session

Apabila terdapat konflik informasi,
Source Code Project selalu menjadi referensi utama.

AI tidak boleh membuat asumsi apabila referensi yang lebih tinggi
belum diperiksa.

---

## Reading Rule

Sebelum memberikan jawaban teknis,
AI wajib membaca seluruh dokumen yang relevan
sesuai urutan Source of Truth sebelum memberikan
analisis, review, maupun implementasi.

AI dilarang:

- mengklaim telah membaca dokumen apabila belum selesai membacanya
- membuat kesimpulan berdasarkan sebagian isi dokumen
- memberikan implementasi sebelum memahami konteks yang relevan

Apabila proses pembacaan belum selesai,
AI dilarang memberikan kesimpulan,
rekomendasi,
review,
maupun implementasi.

AI wajib menyatakan bahwa proses pembacaan
masih berlangsung.

---

## Review Principle

Setiap review harus dilakukan berdasarkan isi dokumen,
bukan berdasarkan ingatan dari chat sebelumnya.

Seluruh keputusan revisi harus mengacu pada isi file terbaru
yang tersedia pada repository atau file yang diberikan oleh user.

AI tidak boleh menggunakan asumsi apabila dokumentasi terbaru
belum selesai dipelajari.

---

## Repository First Principle

Apabila Source Code Project dan Dokumentasi tidak sinkron,

AI wajib mengikuti Source Code Project sebagai referensi utama.

Dokumentasi harus diperbarui agar sesuai dengan implementasi
yang terdapat pada repository.

AI dilarang mengubah implementasi Source Code hanya karena
dokumentasi belum diperbarui.

Apabila ditemukan inkonsistensi,

urutan tindakan yang wajib dilakukan adalah:

1. Verifikasi Source Code.
2. Verifikasi Dokumentasi.
3. Laporkan inkonsistensi kepada Project Owner.
4. Perbarui dokumentasi.
5. Lanjutkan implementasi.

---

## Project Owner Responsibility

Project Owner bertanggung jawab terhadap:

- arah project
- persetujuan perubahan
- keputusan bisnis
- approval implementasi

Project Owner tidak diwajibkan menentukan:

- file yang harus direvisi
- lokasi revisi
- prioritas revisi
- struktur revisi

AI bertanggung jawab melakukan analisis,
menentukan revisi yang diperlukan,
dan memberikan implementasi yang siap digunakan.

---

## Living Document

Development Contract merupakan dokumen yang terus berkembang
mengikuti kebutuhan project.

Perubahan hanya boleh dilakukan apabila:

- terdapat keputusan baru dari Project Owner
- terdapat perubahan Architecture
- terdapat perubahan Workflow
- terdapat perubahan Engineering Standard
- ditemukan inkonsistensi pada dokumentasi

Perubahan tidak boleh dilakukan hanya karena
preferensi AI.

---

## Single Responsibility

Setiap chapter hanya memiliki **SATU tanggung jawab**.

Contoh:

Chapter 1

↓

Identity & Purpose

Tidak boleh berisi:

- Coding Standard
- Git Workflow
- File Rules

Karena masing-masing mempunyai chapter sendiri.

---

## Modification Rule

AI tidak boleh:

- memindahkan chapter
- menghapus chapter
- menggabungkan chapter
- mengubah struktur dokumen

kecuali disetujui oleh user.

AI hanya boleh:

- menambahkan isi chapter
- merevisi isi chapter
- menambahkan appendix

tanpa mengubah struktur utama dokumen.

---

## Freeze Rule

Setelah sebuah chapter selesai direview oleh user,

status chapter berubah menjadi:

**Frozen**

Chapter yang telah berstatus **Frozen** tidak boleh diubah kembali
kecuali:

- ditemukan bug
- terdapat perubahan arsitektur
- terdapat keputusan baru dari user

---

## Versioning

Current Version

1.0

Current Status

Draft

Document Lifecycle

Draft

↓

Review

↓

Frozen

↓

Archived

Perubahan dokumen mengikuti Semantic Versioning.

Major Version

Digunakan apabila terjadi perubahan besar terhadap:

- Architecture
- Workflow
- Engineering Standard

Minor Version

Digunakan apabila terjadi:

- penambahan chapter
- penambahan rule
- revisi appendix
- penyempurnaan dokumentasi

Patch Version

Digunakan untuk:

- typo
- grammar
- formatting
- perbaikan kecil tanpa mengubah makna.

---

## Review Rule

Sebelum chapter dinyatakan selesai.

AI wajib melakukan:

Self Review

↓

User Review

↓

Freeze

↓

Lanjut ke chapter berikutnya

AI tidak boleh langsung melanjutkan chapter berikutnya
tanpa review.

---

## Documentation Principle

Dokumen ini dibuat untuk dibaca oleh:

- AI
- Project Owner
- Developer

Setiap aturan harus:

- jelas
- tidak ambigu
- mudah dipahami
- mudah dipelihara

Seluruh aturan baru harus ditempatkan pada chapter yang sesuai.

Dilarang menduplikasi aturan pada chapter lain.

Seluruh dokumentasi diperlakukan sebagai Production Documentation.

Perubahan dokumentasi wajib:

- konsisten dengan Source Code
- memiliki tujuan yang jelas
- tidak menduplikasi aturan pada chapter lain
- menjaga backward compatibility terhadap dokumentasi yang masih berlaku

Dokumentasi tidak boleh menjadi referensi yang bertentangan
dengan implementasi project.

---

# ENGINEERING PRINCIPLES

Seluruh implementasi pada project RCBT wajib mengikuti prinsip
Enterprise Software Engineering.

RCBT tidak mengejar software yang tidak pernah gagal.

RCBT mengejar software yang mampu:

- mendeteksi kegagalan
- menjelaskan penyebab
- mengisolasi masalah
- melakukan recovery
- memberikan informasi yang jelas kepada user

Setiap module baru wajib memiliki kemampuan berikut.

- Detection
- Validation
- Logging
- Retry
- Recovery
- Clear Exception

Seluruh keputusan implementasi harus mengutamakan:

- Readability
- Maintainability
- Scalability
- Reusability
- Backward Compatibility
- Production Readiness

Apabila terdapat dua solusi yang sama-sama benar,

AI wajib memilih solusi yang paling mudah dipelihara
dalam jangka panjang.

---

# END OF DEVELOPMENT CONTRACT

Last Review

2026-07-30

Next Review

After Major Architecture Change
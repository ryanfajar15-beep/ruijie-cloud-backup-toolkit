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

# Project Identity


Project:

Ruijie Cloud Backup Toolkit (RCBT)


Type:

Production-grade automation toolkit



Tujuan:


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

├── HISTORY/

├── DECISIONS/

└── TROUBLESHOOTING/



---

# Context Reading Order


Saat membuka chat baru:


1. Baca:


docs/CHAT_BOOTSTRAP.md



2. Baca:


docs/SESSION_CONTEXT.md



3. Baca history phase terakhir:


docs/HISTORY/



4. Jika membutuhkan keputusan:


docs/DECISIONS/



5. Jika membutuhkan error sebelumnya:


docs/TROUBLESHOOTING/



Tujuan:


Melanjutkan dari kondisi terakhir.


Tidak mengulang investigasi yang sudah selesai.



---

# Core Architecture


Workflow utama:


incoming/


    |

    v


backup.py


    |

    v


Workspace


    |

    v


Parser


    |

    v


Authentication


    |

    v


API Client


    |

    v


Backup Workflow


    |

    v


Report



---

# Main Controller Rule


backup.py adalah controller utama.


Tanggung jawab:


- menjalankan workflow
- menghubungkan module



backup.py tidak boleh:


- parsing HAR
- authentication logic
- API implementation detail
- download logic
- report generation logic



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


- credential handling
- login flow
- session management



Tidak melakukan:


- backup workflow
- HAR parsing



---

## API Client


Bertanggung jawab:


- komunikasi API
- request handling
- response handling



Tidak melakukan:


- login decision
- workflow business logic



---

## Backup


Bertanggung jawab:


- menjalankan proses backup
- menggunakan API Client
- menyimpan hasil backup



Tidak melakukan:


- membaca HAR langsung
- authentication





---

# Phase Lifecycle Management


## Phase Structure


RCBT menggunakan struktur phase:


Major Phase:


Phase X



Sub Phase:


Phase X.Y



Contoh:


Phase 6


    |

    +-- Phase 6.1 API Client Base


    |

    +-- Phase 6.2 Render Client


    |

    +-- Phase 6.3 Authentication Flow Discovery



---

# Phase Status Definition


Setiap phase memiliki status:


PLANNING


Belum dimulai.



IN PROGRESS


Sedang berjalan.



BLOCKED


Terhenti karena dependency atau masalah.



COMPLETED


Selesai dan sudah terdokumentasi.



---

# Current Phase Rule


Status phase aktif tidak ditentukan dari CHAT_BOOTSTRAP.md.


Sumber utama:


docs/SESSION_CONTEXT.md



SESSION_CONTEXT.md harus menjadi referensi:


- phase aktif
- sub phase aktif
- task berjalan
- blocker
- next action



---

# Phase Completion Rule


Major phase tidak boleh dianggap selesai jika masih ada sub phase yang belum selesai.



Contoh:


Phase 6:


Status:

IN PROGRESS



Karena:


Phase 6.3 Authentication Flow Discovery


Status:

IN PROGRESS



---

# Moving Phase Rule


Tidak boleh pindah ke phase berikutnya sebelum:


[ ] Semua sub phase selesai


[ ] Testing selesai


[ ] Error penting tercatat


[ ] Technical decision tercatat


[ ] History document dibuat


[ ] SESSION_CONTEXT.md diperbarui



---

# Development Workflow


Setiap perubahan mengikuti:


Analysis


    |


    v


Design Decision


    |


    v


Implementation


    |


    v


Testing


    |


    v


Documentation


    |


    v


Git Commit



---

# Implementation Execution Rule


Jika tidak ada perubahan repository:


Berikan:


- analisa
- penjelasan
- keputusan teknis



Jika membutuhkan perubahan repository:


Berikan:


- executable command
- validation command
- git command jika diperlukan



---

# File Modification Rule


Untuk perubahan file:


Prioritas:


1. Python automation


2. Python replacement


3. Full file generator


4. Heredoc



Hindari:


- nano untuk file panjang
- edit cursor manual
- mencari lokasi baris secara manual
- copy paste block ke tengah file



Tujuan:


- reproducible
- mengurangi human error
- menjaga konsistensi



---

# Long File Rule


File panjang harus diberikan:


Part 1/x


Part 2/x


Part 3/x



Setiap part:


- langsung dapat dijalankan
- memiliki urutan jelas
- tidak membutuhkan edit manual





---

# Documentation Automation Rule


Dokumentasi adalah bagian dari development.


Dokumentasi bukan pekerjaan tambahan setelah coding selesai.



---

# Phase Documentation Output


Setiap phase selesai wajib menghasilkan:


## History Document


Lokasi:


docs/HISTORY/


Format:


PHASE_<NUMBER>_<NAME>.md



Isi minimal:


- Overview
- Objective
- Implementation
- Investigation
- Error History
- Solution
- Technical Decision
- Architecture Impact
- Testing Result
- Phase Result
- Next Phase



---

# Decision Documentation


Keputusan architecture penting harus dicatat.


Lokasi:


docs/DECISIONS/



Format:


ADR_<NUMBER>_<NAME>.md



Isi:


## Problem


Masalah yang membutuhkan keputusan.



## Context


Kondisi ketika keputusan dibuat.



## Options Considered


Pilihan solusi yang dianalisa.



## Decision


Keputusan final.



## Reason


Alasan memilih keputusan tersebut.



## Impact


Dampak terhadap:


- architecture
- module
- workflow
- maintenance



---

# Troubleshooting Documentation


Error penting harus dicatat.


Lokasi:


docs/TROUBLESHOOTING/



Format:


PHASE_<NUMBER>_ERRORS.md



Isi:


## Error


Pesan error.



## Investigation


Proses analisa.



## Root Cause


Penyebab utama.



## Solution


Perbaikan.



## Prevention


Cara mencegah masalah yang sama.



---

# Engineering Memory Rule


Selama development phase berjalan, informasi penting harus dianggap sebagai engineering history.


Yang harus dicatat:


- error yang muncul
- command troubleshooting
- hasil investigasi
- keputusan teknis
- alternatif solusi
- solusi yang ditolak
- perubahan architecture
- kesepakatan development



Tujuan:


Agar chat baru atau engineer lain dapat memahami alasan sebuah keputusan dibuat.



---

# AI Continuation Rule


Saat melanjutkan RCBT:


AI harus:


- membaca context terlebih dahulu
- memahami phase aktif
- menjaga architecture existing
- mengikuti keputusan sebelumnya
- menjaga backward compatibility
- tidak mengulang investigasi yang sudah selesai



---

# AI Response Rule


Jika hanya membutuhkan diskusi:


Berikan:


- analisa
- pertimbangan
- rekomendasi



Jika membutuhkan perubahan repository:


Berikan langsung:


1. Action


Create / Update / Replace



2. File path



3. Executable command



4. Validation command



5. Git command jika diperlukan



---

# Response Priority


Urutan prioritas:


1. Executable command


2. Validation


3. Git workflow


4. Explanation



Penjelasan diberikan jika:


- ada keputusan architecture
- ada tradeoff
- ada risiko teknis
- ada alasan perubahan



---

# Reproducible Change Rule


Setiap perubahan harus dapat diulang dari terminal.


Contoh:


Create file:


Python generator



Update file:


Python replacement



Large document:


Part based command



Validation:


Explicit test command





---

# Git Workflow Rule


Setiap milestone development harus melalui Git workflow.



Workflow:


Check status:


git status



Stage:


git add <file>



Commit:


git commit -m "<message>"



Push:


git push



---

# Commit Principle


Commit harus menjelaskan perubahan.


Contoh:


phase 06.3: implement authentication client



docs: update phase documentation



fix: resolve session handling issue



---

# Chat Transfer Protocol


Ketika pindah chat:


Jangan menjelaskan ulang seluruh history secara manual.



Upload:


docs/CHAT_BOOTSTRAP.md


docs/SESSION_CONTEXT.md


dan history phase terakhir jika diperlukan.



---

# New Chat Startup Rule


Chat baru harus memahami:


1. Project identity


2. Architecture existing


3. Current phase


4. Active task


5. Previous decision


6. Development workflow



Sumber:


CHAT_BOOTSTRAP.md


untuk aturan.


SESSION_CONTEXT.md


untuk posisi terakhir.



---

# Phase Completion Final Checklist


Sebelum phase dinyatakan COMPLETED:


Development:


[ ] Objective tercapai


[ ] Implementation selesai


[ ] Testing berhasil


[ ] Tidak ada unresolved blocker



Investigation:


[ ] Investigasi tercatat


[ ] Error tercatat


[ ] Solution tercatat



Documentation:


[ ] HISTORY document dibuat


[ ] DECISION document dibuat jika diperlukan


[ ] TROUBLESHOOTING dibuat jika diperlukan



Context:


[ ] SESSION_CONTEXT.md diperbarui


[ ] CHAT_BOOTSTRAP.md diperbarui jika ada perubahan workflow



Git:


[ ] Commit dibuat


[ ] Push berhasil



---

# RCBT Engineering Principle


RCBT dikembangkan sebagai production-grade toolkit.


Prioritas:


1. Clean Architecture


2. Single Responsibility Principle


3. Modular Design


4. Maintainability


5. Scalability


6. Backward Compatibility


7. Reproducible Development


8. Complete Engineering Documentation



---

# Final Rule


Jangan membuat perubahan hanya karena terlihat lebih mudah.


Setiap perubahan harus mempertimbangkan:


- architecture impact
- maintenance impact
- future scalability
- backward compatibility



RCBT harus tetap berkembang sebagai toolkit yang dapat digunakan untuk banyak project dan customer.



---

# End Of CHAT_BOOTSTRAP


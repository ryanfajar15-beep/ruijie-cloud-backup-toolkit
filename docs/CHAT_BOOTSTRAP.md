# RCBT CHAT BOOTSTRAP

# Ruijie Cloud Backup Toolkit (RCBT)


## Purpose


File ini adalah entry point utama ketika melanjutkan project RCBT dari chat baru.


Tujuan file ini:


- memberikan context terakhir project
- menjaga konsistensi architecture
- menyimpan aturan development
- menjelaskan workflow engineering
- memastikan dokumentasi selalu mengikuti perubahan code



---

# Project Identity


Project:

Ruijie Cloud Backup Toolkit (RCBT)


Type:

Production-grade automation toolkit


Purpose:


RCBT dibuat untuk melakukan:


- membaca export HAR
- melakukan API discovery
- memahami workflow internal Ruijie Cloud
- mengelola authentication
- menjalankan backup automation
- menghasilkan output dan report



---

# Source of Truth


Repository adalah sumber utama project.


ChatGPT tidak menggunakan history chat lama sebagai memory permanen.


Karena itu project context disimpan pada:


docs/


Dengan struktur:


docs/

├── CHAT_BOOTSTRAP.md

├── SESSION_CONTEXT.md

├── HISTORY/

├── DECISIONS/

└── TROUBLESHOOTING/



---

# Context Reading Order


Saat membuka chat baru, lakukan:


1. Baca:


docs/CHAT_BOOTSTRAP.md



2. Baca:


docs/SESSION_CONTEXT.md



3. Baca history:


docs/HISTORY/



4. Jika membutuhkan keputusan teknis:


docs/DECISIONS/



5. Jika membutuhkan masalah sebelumnya:


docs/TROUBLESHOOTING/



Tujuan:


Melanjutkan project dari posisi terakhir.


Jangan mengulang investigasi yang sudah selesai.



---

# Current Development Philosophy


RCBT bukan script sekali pakai.


RCBT dikembangkan sebagai toolkit dengan:


- modular architecture
- reusable component
- separation of responsibility
- maintainable workflow
- documented decision



---

# Core Architecture


Workflow utama:


incoming/


    |


    v


backup.py


    |


    v


Workspace Manager


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


backup.py adalah Main Controller.


Tanggung jawab:


- menjalankan workflow
- menghubungkan module


backup.py tidak boleh:


- parsing HAR
- melakukan authentication logic
- membuat API request detail
- melakukan download logic
- membuat report logic



---

# Module Responsibility Rule


Setiap module hanya memiliki satu tanggung jawab.



Parser:


Membaca dan memproses data.



Workspace:


Mengelola workspace.



Authentication:


Mengelola session dan credential.



API Client:


Komunikasi dengan API.



Backup:


Menjalankan proses backup.



Report:


Menghasilkan laporan.



Jangan memindahkan tanggung jawab antar module tanpa keputusan architecture.



---

# Architecture Change Rule


Perubahan architecture tidak boleh dilakukan secara spontan.


Sebelum perubahan besar:


1. Jelaskan masalah.

2. Analisa pilihan solusi.

3. Tentukan keputusan.

4. Dokumentasikan impact.



Semua perubahan architecture harus memiliki decision record.



---

# Current Phase Status


Completed:


Phase 1

Project Bootstrap



Phase 2

Workspace Manager



Phase 3

HAR Import & Parser



Phase 4

Request Discovery & API Mapping



Phase 5

Authentication Strategy



Phase 6

API Client Implementation



Current Target:


Phase 7

Backup Workflow Implementation

# Development Workflow


## General Development Rule


Setiap perubahan RCBT harus mengikuti workflow:


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

# Implementation Style


Saat memberikan perubahan code atau document:


Prioritas:


1. Command yang langsung dapat dijalankan.


2. File generation menggunakan script.


3. Full replacement untuk perubahan besar.


4. Validation command setelah perubahan.



Hindari:


- instruksi edit manual panjang
- mencari nomor baris secara manual
- copy paste potongan code ke tengah file
- perubahan yang membutuhkan banyak cursor movement



Tujuan:


- mengurangi human error
- menjaga indentation
- menjaga reproducibility
- mempercepat workflow



---

# File Modification Method


Untuk perubahan file gunakan:


## Small Change


Gunakan:

- Python replace
- automated update script



## Large Change


Gunakan:


- Python full file generator
- heredoc
- Part 1/x, Part 2/x



Contoh workflow:


Generate File


    |

    v


Run Validation


    |

    v


Commit



---

# Documentation Writing Rule


Dokumentasi adalah bagian dari development.


Dokumentasi bukan pekerjaan tambahan setelah project selesai.



Setiap perubahan besar harus memiliki:


- alasan perubahan
- implementasi
- testing
- impact
- keputusan teknis



---

# Phase Documentation Rule


Setiap phase yang selesai wajib menghasilkan:


docs/HISTORY/PHASE_<NUMBER>_<NAME>.md



Dokumen phase harus berisi:


## Overview


Tujuan phase.



## Objective


Target yang ingin dicapai.



## Implementation


Apa yang dibuat.


Meliputi:


- module baru
- perubahan file
- workflow baru



## Investigation


Catatan investigasi:


- data yang ditemukan
- analisa API
- hasil eksperimen
- observasi penting



## Error History


Semua error penting dicatat:


- error message
- lokasi error
- penyebab
- solusi



## Technical Decision


Catatan keputusan:


- problem
- opsi solusi
- keputusan final
- alasan memilih solusi



## Architecture Impact


Perubahan terhadap:


- module
- workflow
- dependency
- responsibility



## Testing Result


Berisi:


- command testing
- hasil testing
- validation status



## Phase Result


Status:


COMPLETED



## Next Phase


Target development berikutnya.



---

# Phase Memory Capture Rule


Selama sebuah phase berjalan, semua informasi penting dianggap sebagai bagian dari engineering history.


Yang harus diperhatikan:


- error yang muncul
- troubleshooting
- percobaan yang dilakukan
- solusi yang berhasil
- solusi yang ditolak
- keputusan design
- perubahan arah development
- kesepakatan architecture



Tujuan:


Agar ketika pindah chat, history engineering tetap tersedia.



---

# AI Working Behavior


Saat melanjutkan project:


AI harus:


- membaca context sebelum memberikan solusi
- menjaga architecture existing
- mengikuti keputusan sebelumnya
- tidak mengulang investigasi lama
- mempertahankan naming convention
- menjaga backward compatibility



AI tidak boleh:


- mengubah struktur project tanpa diskusi
- membuat module baru tanpa alasan
- memindahkan responsibility antar module tanpa keputusan



---

# Response Format For Implementation


Untuk perubahan code:


Gunakan format:


📌 Phase X.X


Update File

-----------


Command executable



Validation

----------


Command test



Git

---


Command commit



---

# Long File Rule


Jika file panjang:


Gunakan:


Part 1/x

Part 2/x

Part 3/x



Setiap part harus:


- langsung dapat dipaste
- memiliki urutan jelas
- tidak membutuhkan edit manual



---

# Current Development Preference


Preferred:


- terminal command
- Python automation
- reproducible change
- explicit validation



Avoid:


- manual file editing
- ambiguous instruction
- partial modification tanpa context



# Decision Management Rule


## Purpose


Setiap keputusan teknis harus memiliki alasan yang jelas.


Keputusan tidak hanya menyimpan hasil akhir, tetapi juga proses berpikir yang menghasilkan keputusan tersebut.



---

# Decision Record


Untuk keputusan penting gunakan:


docs/DECISIONS/



Format:


ADR_<NUMBER>_<NAME>.md



Isi:


## Problem


Masalah yang membutuhkan keputusan.



## Context


Kondisi saat keputusan dibuat.



## Options Considered


Pilihan solusi yang dianalisa.



## Decision


Solusi yang dipilih.



## Reason


Alasan pemilihan solusi.



## Impact


Dampak terhadap:


- architecture
- module
- workflow
- maintenance



---

# Troubleshooting Documentation Rule


Error penting harus disimpan.


Lokasi:


docs/TROUBLESHOOTING/



Format:


PHASE_<NUMBER>_ERRORS.md



Isi:


## Error


Pesan error yang muncul.



## Investigation


Proses pencarian penyebab.



## Root Cause


Penyebab utama.



## Solution


Perbaikan yang dilakukan.



## Prevention


Cara mencegah error yang sama.



---

# Engineering History Rule


History phase bukan hanya laporan hasil.


History harus menyimpan perjalanan engineering.


Termasuk:


- percobaan
- investigasi
- error
- solusi
- perubahan keputusan
- alasan perubahan



Tujuan:


Engineer lain atau chat baru dapat memahami kenapa sebuah keputusan dibuat.



---

# Authentication Decision Rule


Authentication harus tetap terpisah dari API Client.


Flow:


Credential


    |


    v


Authentication Layer


    |


    v


Session


    |


    v


API Client



API Client tidak boleh:


- mengelola login
- menyimpan credential
- membuat authentication decision



---

# API Communication Rule


Semua komunikasi Ruijie Cloud harus melalui layer API Client.


Flow:


Application


    |


    v


API Client


    |


    v


Webproxy Gateway


    |


    v


Internal API



Tidak melakukan HTTP request langsung dari controller.



---

# Parser Rule


Parser hanya bertanggung jawab:


- membaca data
- normalisasi data
- ekstraksi informasi



Parser tidak:


- melakukan authentication
- melakukan API request
- menjalankan backup



---

# Workspace Rule


Workspace bertanggung jawab:


- project isolation
- folder management
- metadata project
- lifecycle workspace



Workspace tidak:


- parsing
- authentication
- backup processing



---

# Backup Workflow Rule


Backup module bertanggung jawab:


- menjalankan proses backup
- menggunakan API Client
- mengatur alur backup



Backup module tidak:


- membaca HAR langsung
- melakukan login
- mengetahui detail API internal



---

# Testing Requirement


Setiap perubahan code wajib memiliki validation.


Minimal:


Syntax validation:


python -m py_compile <file>



Import validation:


PYTHONPATH=. python -c "from module import Class"



Functional test jika diperlukan.



Testing result harus masuk dokumentasi phase.

# Phase Completion Checklist


Sebuah phase hanya dianggap selesai jika semua kondisi terpenuhi.



## Development


[ ] Objective phase tercapai


[ ] Implementation selesai


[ ] Code sudah divalidasi


[ ] Tidak ada unresolved error



---


## Investigation


[ ] Investigasi penting tercatat


[ ] Temuan teknis dicatat


[ ] API / workflow discovery dicatat jika ada



---


## Documentation


Wajib dibuat:


[ ] docs/HISTORY/PHASE_<NUMBER>_<NAME>.md


Jika ada keputusan penting:


[ ] docs/DECISIONS/



Jika ada error penting:


[ ] docs/TROUBLESHOOTING/



---


## Context Update


Update:


[ ] docs/SESSION_CONTEXT.md


Berisi:


- Current Phase
- Completed Work
- Last Achievement
- Important Decision
- Known Issue
- Next Target



Update:


[ ] docs/CHAT_BOOTSTRAP.md


Berisi:


- Current Status
- Completed Phase
- Next Development Target



---


# Git Workflow Rule


Setiap phase memiliki milestone commit.



Format:


phase XX: <description>



Contoh:


phase 07: implement backup workflow



Workflow:


git status


    |


    v


git add


    |


    v


git commit


    |


    v


git push



---

# Chat Transfer Rule


Ketika pindah chat:


Jangan menjelaskan ulang seluruh history.


Gunakan:


docs/CHAT_BOOTSTRAP.md


sebagai entry point.



Chat baru harus memahami:


- posisi terakhir project
- phase aktif
- architecture
- keputusan sebelumnya
- aturan development



---

# AI Continuation Instruction


Saat melanjutkan RCBT:


AI harus:


- membaca context terlebih dahulu
- mengikuti architecture existing
- menjaga backward compatibility
- menggunakan workflow yang sudah disepakati
- membuat dokumentasi setelah phase selesai



AI tidak boleh:


- menghapus keputusan lama tanpa alasan
- mengganti architecture secara sepihak
- membuat implementasi tanpa validation
- melewati dokumentasi phase



---

# Final Project Principle


RCBT dibangun sebagai production-grade toolkit.


Prioritas:


1. Clean Architecture


2. Single Responsibility Principle


3. Maintainability


4. Scalability


5. Reproducibility


6. Complete Engineering Documentation



---

# End Of CHAT_BOOTSTRAP


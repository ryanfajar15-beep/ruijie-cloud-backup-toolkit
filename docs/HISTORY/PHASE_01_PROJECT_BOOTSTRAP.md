# RCBT HISTORY

# PHASE 01 - PROJECT BOOTSTRAP


## Overview

Phase 1 merupakan tahap awal pembentukan Ruijie Cloud Backup Toolkit (RCBT).

Tujuan utama:

Membangun fondasi toolkit yang modular, scalable, dan dapat digunakan kembali untuk proses backup project Ruijie Cloud.


## Project Objective

RCBT dibuat untuk:

- membaca hasil export HAR dari browser
- melakukan discovery API Ruijie Cloud
- memahami workflow internal aplikasi
- melakukan automation backup
- menghasilkan report


## Core Design Principle

RCBT tidak dibuat sebagai script sekali pakai.

Project dirancang sebagai toolkit dengan:

- modular architecture
- separation of responsibility
- reusable components
- maintainable workflow


## Initial Architecture

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

API Mapping

|
v

Backup

|
v

Report




## Module Responsibility

### backup.py

Role:

Main Controller


Responsibility:

- menjalankan workflow utama
- menghubungkan semua module


Tidak melakukan:

- parsing HAR
- authentication logic
- download logic


---

### development/

Berisi seluruh logic utama project.


Struktur awal:


development/

├── parser
├── workspace
├── downloader
├── exporter
└── report




## Development Rules

Aturan utama:

1. Satu module satu tanggung jawab.

2. Tidak melakukan hardcode path.

3. Konfigurasi dipisahkan dari logic.

4. Perubahan mengikuti Git workflow.

5. Backward compatibility harus dijaga.


## Git Workflow

Repository menggunakan:

- main branch
- commit per milestone
- dokumentasi mengikuti perubahan code


## Initial Folder Concept


incoming/

Tempat file input dari user.

Contoh:

HAR export

projects/

Workspace hasil proses.

output/

Hasil generate.

release/

Build atau package final.




## Phase 1 Result

Status:

COMPLETED


Hasil:

- project structure terbentuk
- workflow architecture ditentukan
- module responsibility ditetapkan
- development guideline dibuat


## Next Phase

Phase 2:

Workspace Manager

Focus:

- membuat project workspace otomatis
- mengelola path
- menyimpan metadata project

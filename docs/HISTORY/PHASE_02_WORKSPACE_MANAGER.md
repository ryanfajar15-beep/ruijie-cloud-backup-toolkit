# RCBT HISTORY

# PHASE 02 - WORKSPACE MANAGER


## Overview

Phase 2 merupakan tahap pembentukan Workspace Manager.

Tujuan utama:

Membuat layer khusus yang bertanggung jawab terhadap pengelolaan workspace project.

Workspace Manager menjadi pemisah antara:

- file input user
- proses parsing
- hasil proses backup


## Problem Before Workspace Manager

Pada tahap awal, proses masih berpotensi bergantung langsung kepada lokasi file input.

Masalah:

- path sulit dikontrol
- struktur output tidak konsisten
- sulit menjalankan banyak project/customer
- metadata project tidak terdokumentasi


## Design Decision

RCBT tidak bekerja langsung pada folder input.

Flow diperbaiki menjadi:


incoming/

    |

    v

Workspace Manager

    |

    v

Project Workspace

    |

    v

Parser


Workspace menjadi boundary setiap proses.


## Workspace Responsibility

Workspace Manager bertanggung jawab untuk:

- membuat workspace project
- mengatur struktur folder
- mengelola path
- menyimpan informasi project
- menyiapkan lokasi kerja untuk module berikutnya


Workspace Manager tidak melakukan:

- parsing HAR
- authentication
- API request
- backup download
- report generation


## Module Structure

Implementasi:


development/workspace/

├── __init__.py

├── workspace.py

├── path_manager.py

├── project_info.py

├── project_writer.py

└── har_importer.py


## Module Responsibility


## workspace.py

Role:

Workspace Controller


Responsibility:

- membuat dan mengatur workspace lifecycle
- menghubungkan path manager dan project metadata


## path_manager.py

Role:

Path Management


Responsibility:

- membuat standard path
- menghindari hardcoded directory
- menyediakan lokasi folder project


## project_info.py

Role:

Project Metadata


Responsibility:

Menyimpan informasi project:

- project name
- project identifier
- source information
- timestamps


## project_writer.py

Role:

Project File Writer


Responsibility:

- menulis metadata project
- membuat file informasi workspace


## har_importer.py

Role:

HAR Input Handler


Responsibility:

- menerima file HAR
- mempersiapkan data untuk parser


Tidak melakukan:

- API discovery
- authentication analysis


## Workspace Structure


Setiap project memiliki workspace:


projects/

└── <project_id>/

    ├── input/

    ├── workspace/

    ├── output/

    └── report/


Struktur ini memungkinkan:

- multiple project support
- isolated processing
- reproducible workflow


## Architecture Impact


Sebelum:


HAR File

    |

    v

Parser


Sesudah:


HAR File

    |

    v

Workspace Manager

    |

    v

Parser


Benefit:

- lifecycle lebih jelas
- module lebih terpisah
- mudah dikembangkan


## Development Principle Applied


Single Responsibility Principle:

Workspace hanya mengelola workspace.


Parser hanya membaca dan memproses data.


Authentication hanya menangani session.


Backup hanya melakukan proses backup.


## Phase 2 Result


Status:

COMPLETED


Hasil:

- workspace layer terbentuk
- path management dipisahkan
- project metadata diperkenalkan
- workflow project menjadi scalable


## Next Phase


Phase 3:

HAR Import & Parser


Focus:

- membaca HAR
- ekstraksi request
- normalisasi data
- membangun parser pipeline





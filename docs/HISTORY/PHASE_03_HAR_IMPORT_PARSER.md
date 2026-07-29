# RCBT HISTORY

# PHASE 03 - HAR IMPORT & PARSER


## Overview

Phase 3 merupakan tahap pembangunan engine pembacaan dan pemrosesan HAR (HTTP Archive).

Tujuan utama:

Membuat pipeline parser yang mampu:

- membaca file HAR hasil browser export
- mengambil request data
- melakukan filtering request
- melakukan klasifikasi request
- melakukan normalisasi endpoint
- menghasilkan catalog data


## Problem Before Parser

Sebelum parser pipeline dibuat, HAR hanya berupa data mentah.

Permasalahan:

- sulit membaca ribuan request secara manual
- endpoint bercampur dengan asset static
- struktur request berbeda-beda
- sulit melakukan API discovery
- sulit digunakan kembali untuk project berbeda


## Design Decision

RCBT tidak melakukan analisis HAR langsung di controller.

Flow dibuat:


HAR File

    |

    v

HAR Importer

    |

    v

Request Reader

    |

    v

Request Classifier

    |

    v

API Filter

    |

    v

Endpoint Normalizer

    |

    v

Catalog Writer


Setiap module memiliki tanggung jawab tunggal.


## Parser Responsibility

Parser hanya:

- membaca data
- mengekstrak informasi
- mengolah struktur request


Parser tidak:

- melakukan login
- membuat session
- menjalankan API
- melakukan download backup
- menyimpan file hasil backup


## Parser Module Structure


Implementasi:


development/parser/


├── __init__.py


├── modules/

│
├── request_reader.py

├── request_classifier.py

├── api_filter.py

├── endpoint_normalizer.py

├── request_catalog.py

├── catalog_writer.py

├── auth_discovery.py

└── auth_writer.py


├── versions/

│
├── parser_v01.py

├── parser_v02.py

├── parser_v03.py

├── parser_v04.py

└── parser_v05.py



## Module Responsibility


# request_reader.py


Role:

HAR Request Reader


Responsibility:

- membaca entry HAR
- mengambil request object
- menyediakan data request untuk pipeline berikutnya


Input:

HAR entries


Output:

Normalized request list



# request_classifier.py


Role:

Request Classification


Responsibility:

Mengelompokkan request berdasarkan karakteristik.


Contoh kategori:

- API request
- static asset
- external resource
- authentication request


Tujuan:

Memisahkan request penting dari noise.



# api_filter.py


Role:

API Detection


Responsibility:

Mendeteksi request yang kemungkinan merupakan API.


Filter berdasarkan:

- HTTP method
- URL pattern
- endpoint structure
- content type


Output:

API candidate list


# endpoint_normalizer.py


Role:

Endpoint Normalization


Responsibility:

Mengubah berbagai format URL menjadi bentuk endpoint yang konsisten.


Contoh:

Before:

https://cloud-as.ruijienetworks.com/webproxy/common/api?/project/list


After:

/project/list


Tujuan:

- mempermudah API grouping
- menghindari duplicate endpoint
- membuat API catalog lebih bersih



# request_catalog.py


Role:

Request Catalog Model


Responsibility:

Menyediakan struktur data catalog request.


Data yang disimpan:

- endpoint
- method
- module
- request metadata
- source information



# catalog_writer.py


Role:

Catalog Generator


Responsibility:

Menulis hasil parsing menjadi catalog.


Output:

request_catalog.json


Tujuan:

Menyimpan hasil discovery agar dapat digunakan oleh:

- API mapping
- authentication analysis
- backup workflow



# auth_discovery.py


Role:

Authentication Discovery


Responsibility:

Mendeteksi informasi authentication dari HAR.


Yang dianalisa:

- Cookie
- Authorization header
- authentication related endpoint


Hasil:

Authentication metadata



# auth_writer.py


Role:

Authentication Catalog Writer


Responsibility:

Menyimpan hasil discovery authentication.


Output:

Authentication catalog


Tujuan:

Memisahkan informasi authentication dari request catalog utama.



# Parser Versioning


RCBT menggunakan parser versioning.


Lokasi:


development/parser/versions/


Berisi:


parser_v01.py

parser_v02.py

parser_v03.py

parser_v04.py

parser_v05.py



Tujuan versioning:


- menjaga backward compatibility
- memungkinkan perubahan parser tanpa merusak parser lama
- mempermudah migrasi format



# HAR Investigation Result


Testing dilakukan menggunakan HAR Ruijie Cloud.


Input:


cloud-as.ruijienetworks.com_New_300726_00.10.har



Hasil awal:


Total Request:

3405



HTTP Method:


GET:

2916


POST:

486


OPTIONS:

2


PUT:

1



# Host Discovery


Top Host:


cloud-as.ruijienetworks.com


Jumlah:

1096 request



Internal API ditemukan melalui:


/webproxy/common/api



Jumlah:


481 request



# Webproxy Discovery


Ditemukan pola:


POST


https://cloud-as.ruijienetworks.com/webproxy/common/api



Payload:


{
    "api": "/endpoint",
    "method": "GET",
    "module": "module_name",
    "querys": {}
}



Kesimpulan:


Ruijie Cloud menggunakan gateway webproxy sebagai layer API abstraction.


Client tidak langsung memanggil endpoint backend.


Flow:


Frontend

    |

    v

/webproxy/common/api

    |

    v

Internal API Module



# API Discovery Preparation


Hasil parser pada Phase 3 menjadi dasar untuk Phase 4:


Request Discovery & API Mapping


Data yang dihasilkan parser:

- endpoint list
- HTTP method
- module information
- request payload
- authentication metadata




# Authentication Discovery Result


Pada tahap parser awal, RCBT mulai melakukan discovery terhadap informasi authentication.


Investigasi dilakukan terhadap:

- request headers
- request cookies
- authorization header
- login related endpoint



## Initial Finding


HAR export tidak selalu menyediakan credential authentication.


Ditemukan kondisi:


request.headers:

- tidak terdapat Cookie
- tidak terdapat Authorization



request.cookies:


empty



Kesimpulan:

HAR digunakan sebagai sumber discovery API.

HAR bukan sumber utama authentication.



# API Flow Discovery


Dari hasil parser ditemukan pola utama Ruijie Cloud:


Frontend Request

        |

        v

/webproxy/common/api

        |

        v

Internal API Endpoint



Contoh:


POST:

/webproxy/common/api?/plan/render/async/start



Payload:


{
    "api": "/plan/render/async/start",
    "method": "POST",
    "module": "survey",
    "querys": {
        "lang": "en"
    }
}



# Render API Discovery


Parser menemukan workflow render:


## Start Render


Endpoint:


/plan/render/async/start



Method:


POST



Module:


survey



Function:


Memulai proses render asynchronous.



## Render Result


Endpoint:


/plan/render/async/result



Method:


POST



Module:


survey



Function:


Mengambil hasil render setelah proses selesai.



Workflow:


Start Render

    |

    v

Render Job

    |

    v

Poll Result

    |

    v

Render Output



# Parser Output


Hasil Phase 3 menghasilkan data yang digunakan oleh module berikutnya.


Output:


request_catalog.json


Berisi:

- endpoint catalog
- request metadata
- API classification
- module information



Authentication output:


authentication catalog



Berisi:

- authentication discovery result
- detected session information
- authentication metadata



# Phase 3 Result


Status:


COMPLETED



Hasil:


- HAR importer tersedia
- request parsing pipeline tersedia
- request classification tersedia
- API filtering tersedia
- endpoint normalization tersedia
- request catalog generation tersedia
- authentication discovery foundation tersedia



# Architecture Impact


Setelah Phase 3:


Input:


HAR File


        |

        v


Workspace


        |

        v


Parser Pipeline


        |

        +----------------+

        |                |

        v                v


API Catalog       Authentication Metadata



Data hasil parser menjadi input untuk phase berikutnya.



# Lessons Learned


## HAR Limitation


Browser HAR export dapat menghilangkan informasi sensitif.


Karena itu:


Parser:

bertugas discovery.


Authentication:

harus memiliki module sendiri.



## Webproxy Architecture


Ruijie Cloud menggunakan API gateway abstraction.


RCBT harus memahami:


Frontend API

        |

        v

Webproxy Gateway

        |

        v

Internal API



# Next Phase


Phase 4:

Request Discovery & API Mapping



Focus:


- mapping endpoint
- memahami module API
- membuat API catalog
- menentukan backup workflow




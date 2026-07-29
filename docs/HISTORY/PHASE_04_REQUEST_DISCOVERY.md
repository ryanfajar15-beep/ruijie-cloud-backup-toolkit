# RCBT HISTORY

# PHASE 04 - REQUEST DISCOVERY & API MAPPING


## Overview

Phase 4 merupakan tahap analisis request hasil parser untuk memahami struktur API internal Ruijie Cloud.

Tujuan utama:

- melakukan discovery endpoint
- memahami pola komunikasi frontend dengan backend
- melakukan mapping module API
- membangun dasar API catalog


## Input Source


Sumber data:


HAR Export

    |

    v

Parser Output

    |

    v

Request Catalog



Data yang dianalisa:

- URL request
- HTTP method
- payload
- module
- API endpoint
- response information



## Problem Before API Mapping


Pada tahap awal, HAR hanya menghasilkan daftar request.


Permasalahan:

- jumlah request sangat besar
- banyak request bukan API
- endpoint belum terkelompokkan
- hubungan antar API belum diketahui


Contoh:

Satu project dapat menghasilkan ribuan request:


3405 requests


Tidak semua request berhubungan dengan proses backup.



## Design Decision


RCBT tidak melakukan backup berdasarkan URL langsung.


Diperlukan layer:


Request Discovery

        |

        v

API Mapping

        |

        v

Backup Workflow



Tujuan:

Memisahkan proses discovery dengan proses execution.



## Request Discovery Responsibility


Request Discovery bertanggung jawab untuk:


- membaca hasil parser
- mencari request API
- mengelompokkan endpoint
- mengidentifikasi module
- menghasilkan API mapping


Tidak melakukan:


- authentication
- API execution
- download backup
- report generation



## Discovery Result


Berdasarkan HAR Ruijie Cloud:


Total Request:


3405



HTTP Method Distribution:


GET:

2916


POST:

486


OPTIONS:

2


PUT:

1



## Host Discovery


Host utama:


cloud-as.ruijienetworks.com



Jumlah request:


1096



Host lain yang ditemukan:


enet-as.ruijiecloud.net



Jumlah:


706



## API Identification


Ditemukan pola utama:


/webproxy/common/api



Request:


POST


Format:


https://cloud-as.ruijienetworks.com/webproxy/common/api?/endpoint



Payload:


{
    "api": "/endpoint",
    "method": "GET",
    "module": "module_name",
    "querys": {}
}



## Webproxy Architecture


Frontend Application

        |

        v

Webproxy Gateway

        |

        v

Internal API Service



Kesimpulan:

Frontend tidak langsung memanggil backend API.

Semua komunikasi melewati webproxy layer.




# Webproxy Analysis Result


Tool:

tools/analyze_webproxy.py



Command:


PYTHONPATH=. python tools/analyze_webproxy.py



Result:


TOTAL WEBPROXY:

481



METHOD:


POST:

481



## Webproxy Request Pattern


Semua request menggunakan:


POST


Endpoint:


/webproxy/common/api



Contoh:


POST https://cloud-as.ruijienetworks.com/webproxy/common/api?/org/account/info



Payload:


{
    "api": "/org/account/info",
    "method": "GET",
    "module": "default",
    "querys": {
        "lang": "en"
    }
}



## Internal API Extraction


Tool:


tools/extract_internal_api.py



Command:


PYTHONPATH=. python tools/extract_internal_api.py



Result:


TOTAL INTERNAL API:


287 endpoint



## API Frequency Discovery


Endpoint paling sering:


/plan/render/async/result


Jumlah:


287 request



Endpoint lain:


/scheme/region/uplink

23 request



/project/174833

15 request



/project/shelf/list

12 request



/plan/430457

12 request



## Module Mapping Result


Hasil grouping module:


survey:

364 request



schemes:

104 request



enet:

4 request



um:

4 request



mall:

2 request



nps:

2 request



default:

1 request



## API Catalog Direction


Dari hasil discovery, API mulai dapat dikelompokkan berdasarkan fungsi:


Survey Module:

- render
- heatmap
- topology
- measurement



Schemes Module:

- project scheme
- device topology
- product catalog



User Module:

- account
- team member
- user information



## API Mapping Principle


RCBT tidak menyimpan API sebagai daftar URL sederhana.


API catalog harus menyimpan:


- endpoint
- module
- method
- purpose
- dependency
- authentication requirement



Tujuan:

Membentuk dependency map sebelum proses backup.



# Render Workflow Discovery


Salah satu workflow penting yang ditemukan adalah:

Survey Render Process



## Render Start


Endpoint:


/plan/render/async/start



Method:


POST



Module:


survey



Function:


Memulai proses render secara asynchronous.



Payload ditemukan:


{
    "schemeId": "174833",
    "regionInfo": {
        "430457": [
            "surveyPoint",
            "heatmap24",
            "heatmap5",
            "monitor",
            "heatmap6"
        ]
    },
    "version": "v2"
}



## Render Result


Endpoint:


/plan/render/async/result



Method:


POST



Module:


survey



Function:


Mengambil hasil render.



Workflow:


/plan/render/async/start

        |

        v

Render Job Created

        |

        v

/plan/render/async/result

        |

        v

Render Output



## Render Sequence Analysis


Tool:


tools/analyze_render_sequence.py



Command:


PYTHONPATH=. python tools/analyze_render_sequence.py



Output:


analysis/render_sequence.json



Hasil:


- start render request ditemukan
- result polling request ditemukan
- dependency antar request berhasil diidentifikasi



# API Mapping Result


Dari hasil discovery Phase 4, RCBT memiliki dasar API mapping:


## Survey Module


Function:

- render
- heatmap
- topology
- survey data



Important Endpoint:


/plan/render/async/start


/plan/render/async/result


/scheme/device/topo


/heatmap/all/data



## Schemes Module


Function:

- project scheme
- device configuration
- product catalog



Important Endpoint:


/scheme/list


/scheme/info


/scheme/device/topo



## User Module


Function:

- account information
- team member
- user information



Important Endpoint:


/org/account/info


/team_member/self/get


/scheme/user/info



# API Mapping Architecture


Hasil Phase 4:


HAR

 |

 v

Parser

 |

 v

Request Discovery

 |

 v

API Mapping

 |

 v

API Catalog



API Catalog menjadi sumber untuk:


- API Client development
- backup workflow
- dependency analysis



# Phase 4 Result


Status:


COMPLETED



Hasil:


- request discovery pipeline selesai
- webproxy pattern berhasil ditemukan
- internal API berhasil diekstraksi
- module mapping berhasil dibuat
- render workflow berhasil dipahami
- API catalog foundation tersedia



# Key Technical Findings


## 1. Webproxy Gateway


Ruijie Cloud menggunakan:


Frontend

    |

    v

/webproxy/common/api

    |

    v

Internal API



## 2. Authentication Separation


API discovery dapat dilakukan melalui HAR.


Namun execution API membutuhkan authentication layer terpisah.



## 3. Async Workflow


Beberapa proses menggunakan asynchronous pattern.


Contoh:


Start Job

    |

    v

Polling Result

    |

    v

Download / Processing



# Next Phase


Phase 5:

Authentication Strategy


Focus:


- session management
- authentication client
- cookie handling
- API request authorization






# RCBT HISTORY

# PHASE 06 - API CLIENT IMPLEMENTATION


## Overview

Phase 6 merupakan tahap implementasi API Client layer.

Tujuan utama:

Membuat module yang bertanggung jawab untuk komunikasi langsung dengan Ruijie Cloud API melalui webproxy gateway.


## Background


Dari hasil Phase 4:

RCBT berhasil menemukan pola komunikasi:


Frontend

    |

    v

/webproxy/common/api

    |

    v

Internal API



API tidak dipanggil secara langsung.

Semua request melewati webproxy abstraction layer.



## Problem Before API Client


Sebelum API Client dibuat:


- API hanya diketahui melalui hasil discovery
- belum ada module untuk execution
- request masih dilakukan melalui browser
- workflow backup belum dapat melakukan automation



Diperlukan layer:


API Mapping


    |

    v


API Client


    |

    v


Backup Workflow



## Design Decision


RCBT tidak melakukan HTTP request langsung dari controller.


API communication dipisahkan:


backup.py


    |

    v


API Client


    |

    v


Ruijie Cloud API



Tujuan:


- menjaga separation of responsibility
- API client reusable
- memudahkan testing
- menghindari duplikasi request logic



## API Client Responsibility


API Client bertanggung jawab:


- membuat request HTTP
- mengirim payload API
- menangani response
- melakukan polling asynchronous process



API Client tidak:


- membaca HAR
- membuat workspace
- melakukan authentication login
- menyimpan hasil backup
- membuat report



## Module Structure


Implementasi:


development/api/


├── __init__.py

└── render_client.py



## render_client.py


Role:


Render API Client



Responsibility:


- start render job
- polling render result
- extract render metadata



Tidak melakukan:


- download image
- save file
- report generation



## Webproxy Endpoint


Base endpoint:


/webproxy/common/api



Format request:


POST


/webproxy/common/api?/internal_endpoint



Payload:


{
    "api": "/internal_endpoint",
    "method": "POST",
    "module": "module_name",
    "querys": {},
    "params": {}
}



## Session Integration


API Client menggunakan authentication context dari Phase 5.


Flow:


SessionProvider


    |

    v


API Client


    |

    v


Webproxy API



RenderClient tidak mengetahui proses authentication.


RenderClient hanya menggunakan session yang tersedia.



EOF
# RenderClient Implementation


File:


development/api/render_client.py



Class:


RenderClient



## Constructor


RenderClient menerima:


- base_url
- cookies
- timeout



Contoh:


RenderClient(

    base_url="https://cloud-as.ruijienetworks.com",

    cookies=session_cookie

)



Tujuan:


Menyediakan HTTP session yang sudah memiliki authentication context.



## HTTP Session


RenderClient menggunakan:


requests.Session()



Session digunakan untuk:


- menyimpan cookies
- reuse connection
- menjaga request consistency



Headers default:


Accept:

application/json



Content-Type:

application/json



## Endpoint Builder


RenderClient memiliki internal endpoint helper.


Function:


_endpoint()



Responsibility:


Membentuk base webproxy endpoint.



Output:


https://cloud-as.ruijienetworks.com/webproxy/common/api



API path ditambahkan saat request execution.



# Render Start Implementation


## Endpoint


/plan/render/async/start



Method:


POST



Module:


survey



Function:


Memulai proses asynchronous rendering.



Payload structure:


{
    "api": "/plan/render/async/start",
    "method": "POST",
    "module": "survey",
    "querys": {
        "lang": "en"
    },
    "params": {}
}



Parameter utama:


schemeId


regionInfo



## Start Render Flow


Request:


RenderClient


    |

    v


/plan/render/async/start


    |

    v


Render Job Created



Response digunakan sebagai reference untuk proses polling.



# Render Result Implementation


## Endpoint


/plan/render/async/result



Method:


POST



Module:


survey



Function:


Mengambil status dan hasil render.



Payload:


{
    "api": "/plan/render/async/result",
    "method": "POST",
    "module": "survey",
    "querys": {
        "lang": "en"
    },
    "params": {}
}



Parameter utama:


schemeId


regionInfo



# Async Polling Mechanism


Render API menggunakan asynchronous workflow.


Flow:


Start Render


    |

    v


Wait


    |

    v


Request Result


    |

    v


Check Status


    |

    +---- incomplete

    |

    v


Retry


    |

    v


Completed



## wait_render()


Function:


wait_render()



Responsibility:


- melakukan polling result
- menentukan interval
- membatasi retry
- menghentikan ketika selesai



Parameter:


interval


delay antar request



retries


jumlah maksimal polling



# Response Handling


RenderClient melakukan:


- HTTP status validation
- JSON parsing
- response extraction



Function:


response.raise_for_status()



Tujuan:


Menghentikan workflow ketika API response error.



# Image Metadata Extraction


RenderClient memiliki fungsi:


extract_images()



Responsibility:


Mengambil informasi image dari response render.



Tidak melakukan:


- download image
- menyimpan file image



Download menjadi tanggung jawab module berikutnya.



# Validation & Testing


Setelah implementasi RenderClient selesai dilakukan validasi:


## Python Compile Test


Command:


python -m py_compile development/api/render_client.py



Result:


SUCCESS



Tidak terdapat:

- Syntax error
- Import error
- Indentation error



## Import Test


Command:


PYTHONPATH=. python -c "from development.api.render_client import RenderClient; print('OK')"



Result:


OK



Artinya:


- module dapat di-import
- struktur package valid
- class RenderClient tersedia



# Integration With Authentication Layer


Architecture:


Authentication Layer


development/auth/


        |


        v


SessionProvider


        |


        v


API Client


development/api/


        |


        v


RenderClient



Dependency flow:


SessionProvider menyediakan session.


RenderClient menggunakan session.


RenderClient tidak mengelola credential.



# Current API Layer Status


Implemented:


development/api/render_client.py



Available function:


## start_render()


Purpose:


Memulai render process.



## get_render_result()


Purpose:


Mengambil hasil render.



## wait_render()


Purpose:


Polling asynchronous render process.



## extract_images()


Purpose:


Mengambil metadata image dari response.



# Current Limitation


Phase 6 belum melakukan:


- image download
- file storage
- backup packaging
- report generation



Reason:


API Client hanya bertanggung jawab pada komunikasi API.



Feature tersebut akan ditangani oleh phase berikutnya.



# Architecture After Phase 6


Workflow:


Input HAR


    |

    v


Parser


    |

    v


API Catalog


    +


Authentication Session


    |

    v


API Client


    |

    v


Render API


    |

    v


Backup Workflow



# Technical Decision Summary


## Decision 1


API request tidak ditempatkan di backup controller.


Reason:


Menjaga modular architecture.



## Decision 2


Authentication dan API Client dipisahkan.


Reason:


API Client dapat digunakan kembali dengan session berbeda.



## Decision 3


Async API menggunakan polling.


Reason:


Render process membutuhkan waktu dan tidak langsung menghasilkan output.



# Phase 6 Result


Status:


COMPLETED



Hasil:


- API client layer terbentuk
- Render API berhasil dimodelkan
- webproxy communication berhasil diimplementasikan
- authentication dependency dipisahkan
- async render workflow berhasil dipahami
- foundation backup API tersedia



# Next Phase


Phase 7:

Backup Workflow Implementation



Focus:


- mengambil data project
- menjalankan API dependency
- download hasil backup
- menyimpan output
- membuat report
# Validation & Testing


Setelah implementasi RenderClient selesai dilakukan validasi:


## Python Compile Test


Command:


python -m py_compile development/api/render_client.py



Result:


SUCCESS



Tidak terdapat:

- Syntax error
- Import error
- Indentation error



## Import Test


Command:


PYTHONPATH=. python -c "from development.api.render_client import RenderClient; print('OK')"



Result:


OK



Artinya:


- module dapat di-import
- struktur package valid
- class RenderClient tersedia



# Integration With Authentication Layer


Architecture:


Authentication Layer


development/auth/


        |


        v


SessionProvider


        |


        v


API Client


development/api/


        |


        v


RenderClient



Dependency flow:


SessionProvider menyediakan session.


RenderClient menggunakan session.


RenderClient tidak mengelola credential.



# Current API Layer Status


Implemented:


development/api/render_client.py



Available function:


## start_render()


Purpose:


Memulai render process.



## get_render_result()


Purpose:


Mengambil hasil render.



## wait_render()


Purpose:


Polling asynchronous render process.



## extract_images()


Purpose:


Mengambil metadata image dari response.



# Current Limitation


Phase 6 belum melakukan:


- image download
- file storage
- backup packaging
- report generation



Reason:


API Client hanya bertanggung jawab pada komunikasi API.



Feature tersebut akan ditangani oleh phase berikutnya.



# Architecture After Phase 6


Workflow:


Input HAR


    |

    v


Parser


    |

    v


API Catalog


    +


Authentication Session


    |

    v


API Client


    |

    v


Render API


    |

    v


Backup Workflow



# Technical Decision Summary


## Decision 1


API request tidak ditempatkan di backup controller.


Reason:


Menjaga modular architecture.



## Decision 2


Authentication dan API Client dipisahkan.


Reason:


API Client dapat digunakan kembali dengan session berbeda.



## Decision 3


Async API menggunakan polling.


Reason:


Render process membutuhkan waktu dan tidak langsung menghasilkan output.



# Phase 6 Result


Status:


COMPLETED



Hasil:


- API client layer terbentuk
- Render API berhasil dimodelkan
- webproxy communication berhasil diimplementasikan
- authentication dependency dipisahkan
- async render workflow berhasil dipahami
- foundation backup API tersedia



# Next Phase


Phase 7:

Backup Workflow Implementation



Focus:


- mengambil data project
- menjalankan API dependency
- download hasil backup
- menyimpan output
- membuat report

zc

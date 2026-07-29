# RCBT HISTORY

# PHASE 05 - AUTHENTICATION STRATEGY


## Overview

Phase 5 merupakan tahap pemisahan authentication layer dari proses parsing dan API execution.

Tujuan utama:

Membangun mekanisme authentication yang:

- tidak bergantung kepada HAR export
- dapat digunakan kembali oleh API Client
- mendukung automation workflow
- menjaga session lifecycle


## Problem Before Authentication Layer


Pada fase awal discovery, HAR digunakan untuk memahami komunikasi aplikasi.


Namun ditemukan keterbatasan:


- credential tidak selalu tersedia
- cookie dapat disanitasi browser
- authorization header tidak tersedia
- HAR hanya cocok untuk API discovery


Kesimpulan:


HAR bukan sumber authentication utama.



## Investigation Result


Testing dilakukan menggunakan HAR Ruijie Cloud.


Ditemukan:


Request cookie pada HAR:


empty



Authorization header:


tidak ditemukan



Walaupun browser memiliki session aktif, data sensitif tidak selalu ikut dalam export HAR.



## Design Decision


RCBT tidak menggunakan HAR cookie sebagai mekanisme login.


Keputusan:


Authentication harus memiliki module sendiri.


Flow:


Credential

    |

    v

AuthClient

    |

    v

Session

    |

    v

API Client



## Authentication Responsibility


Authentication layer bertanggung jawab:


- membuat session
- menyimpan authentication state
- menyediakan cookie/token untuk API request
- melakukan validation session


Authentication layer tidak:


- parsing HAR
- membaca API catalog
- melakukan backup
- membuat report



## Module Structure


Implementasi:


development/auth/


├── __init__.py

├── auth_validator.py

├── session_provider.py

└── auth_client.py (planned)



## session_provider.py


Role:


Session Management



Responsibility:


- load session data
- menyediakan cookie untuk API client
- menjaga format session



Current implementation:


config/session.json



Example:


{
    "SESSION": "session_value",
    "LT_SESSION": "session_value",
    "SERVERID": "server_value"
}



## Security Consideration


Session data merupakan informasi sensitif.


Aturan:


- tidak disimpan di Git
- tidak dimasukkan ke repository
- hanya digunakan saat runtime


File:


config/session.json



harus tetap local.






# auth_validator.py


Role:


Authentication Validation



Responsibility:


Melakukan validasi terhadap authentication state sebelum API request dijalankan.



Validation yang dilakukan:


- memastikan session tersedia
- memastikan cookie memiliki format valid
- memastikan authentication data dapat digunakan oleh API client



Tujuan:


Menghindari API request gagal karena session tidak valid.



# Session Management Decision


Dari hasil investigasi HAR, terdapat dua pendekatan:


## Option A


Mengambil cookie langsung dari HAR export.



Kelemahan:


- cookie tidak selalu tersedia
- browser dapat melakukan sanitization
- tidak cocok untuk automation
- sulit digunakan pada banyak project



Status:


Rejected



## Option B


Menggunakan authentication session provider.



Flow:


Login / Credential


    |


    v


Session Provider


    |


    v


API Client


    |


    v


Ruijie Cloud API



Status:


Selected



# SessionProvider Implementation


Current module:


development/auth/session_provider.py



Responsibility:


- membaca session configuration
- menyediakan cookie dictionary
- memberikan session object ke API client



Example output:


{
    "SESSION": "value",
    "LT_SESSION": "value",
    "SERVERID": "value"
}



# API Client Integration


Authentication menjadi dependency untuk API client.


Flow:


SessionProvider


        |


        v


RenderClient


        |


        v


/plan/render/async/start


        |


        v


/plan/render/async/result



RenderClient tidak mengetahui bagaimana session dibuat.


RenderClient hanya menggunakan session yang diberikan.



# Security Boundary


Architecture:


development/auth/


    |

    v


Session Management



development/api/


    |

    v


API Communication



Pemisahan ini menjaga:


- authentication logic terisolasi
- API client reusable
- credential tidak tersebar



# Authentication Workflow


Final workflow:


User Credential


    |


    v


AuthClient


    |


    v


SessionProvider


    |


    v


RenderClient


    |


    v


Ruijie Cloud Webproxy API




# Authentication Final Decision


Berdasarkan hasil investigasi:


HAR export:

- digunakan untuk API discovery
- digunakan untuk memahami workflow frontend
- digunakan untuk menemukan endpoint



HAR export bukan digunakan untuk:


- menyimpan credential
- menyimpan session
- menjalankan automation authentication



Keputusan final:


RCBT menggunakan dedicated authentication layer.



# Relationship With API Mapping


Phase 4 menghasilkan:


API Catalog


Berisi:


- endpoint
- module
- method
- request pattern



Phase 5 menyediakan:


Authentication Context


Berisi:


- session
- cookie
- authentication state



Keduanya digabungkan:


API Catalog

        +

Authentication Context

        |

        v

API Execution Layer



# Current Authentication Architecture


Saat ini:


development/auth/


├── auth_validator.py

├── session_provider.py

└── auth_client.py (future)



Responsibility:


auth_validator.py


- validation authentication data



session_provider.py


- menyediakan session runtime



auth_client.py


- menangani proses authentication login
- planned implementation



# Current Limitation


Pada Phase 5:


Authentication login automation belum selesai.


Current approach:


Session dapat diberikan melalui:


config/session.json



Kelebihan:


- cepat untuk testing
- memisahkan credential dari source code
- dapat digunakan oleh API client



Kekurangan:


- session memiliki lifetime
- perlu refresh ketika expired



# Future Development


AuthClient akan menangani:


- login flow
- SSO handling
- session creation
- session refresh
- authentication error handling



Target workflow:


Credential


    |


    v


AuthClient


    |


    v


SessionProvider


    |


    v


API Client



# Phase 5 Result


Status:


COMPLETED



Hasil:


- authentication strategy ditentukan
- HAR cookie dependency dihapus
- session management layer dibuat
- authentication responsibility dipisahkan
- API client dapat menggunakan session provider



# Architecture After Phase 5


Workflow:


HAR

    |

    v

Parser

    |

    v

API Catalog



Credential

    |

    v

Authentication Layer

    |

    v

Session



API Catalog + Session

    |

    v

API Client

    |

    v

Backup Workflow



# Next Phase


Phase 6:

API Client Implementation



Focus:


- membuat API client layer
- implementasi webproxy communication
- render workflow execution
- response handling
- backup API preparation



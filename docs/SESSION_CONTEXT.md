# RCBT Session Context

## Current Phase

Phase: 6.3 - Authentication Flow Discovery


## Project Status

Completed:

- Workspace Manager
- HAR Importer
- Request Reader
- API Discovery
- Endpoint Normalizer
- Authentication Discovery basic
- Render API Client


## Current Architecture

Workflow:

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


## Latest Development

Completed:

### RenderClient

File:

development/api/render_client.py

Status:

- compile OK
- import OK

Test:

python -m py_compile development/api/render_client.py


### SessionProvider

File:

development/auth/session_provider.py

Status:

- created
- tested successfully


## Authentication Investigation

Finding:

Ruijie Cloud does not expose authentication through HAR export.

HAR contains:

- endpoint
- payload
- request sequence

HAR does not reliably contain:

- Cookie
- Authorization


Chrome export uses sanitized HAR.


## Authentication Strategy Decision

Selected:

Option B - Automated Authentication


Target:

Create AuthClient.


Expected flow:

AuthClient

    |
    v

SSO Login

    |
    v

SESSION Cookie

    |
    v

RenderClient


## SSO Discovery Result

Detected:

Login endpoint:

/sso/login


Flow:

GET /sso/login
        |
        v
Login form
        |
        v
POST authentication form
        |
        v
SESSION generated
        |
        v
/webproxy/common/api


Detected fields:

- username
- password
- lt
- sign
- _eventId
- selectedCloud
- googleTotpCode
- disposableCode


## Current Task

Create:

development/auth/auth_client.py


Responsibilities:

- Handle SSO login
- Submit login form
- Retrieve session cookies
- Provide authenticated session


## Next Testing

After AuthClient:

1. Validate login
2. Pass session to RenderClient
3. Execute:

/plan/render/async/start

4. Execute:

/plan/render/async/result


## Notes

Do not move authentication logic into parser.

Parser responsibility:

Only read and analyze HAR data.

"""
Workflow Status Constants
Ruijie Cloud Backup Toolkit (RCBT)
"""

from enum import StrEnum


class ProjectStatus(StrEnum):
    CREATED = "created"
    INITIALIZING = "initializing"
    AUTHENTICATING = "authenticating"
    RENDERING = "rendering"
    DOWNLOADING = "downloading"
    REPORTING = "reporting"
    COMPLETED = "completed"
    FAILED = "failed"
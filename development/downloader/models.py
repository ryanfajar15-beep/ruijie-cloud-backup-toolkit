"""
Downloader Models
Ruijie Cloud Backup Toolkit (RCBT)
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class DownloadStatus(str, Enum):
    """Download process status."""

    PENDING = "PENDING"

    DOWNLOADING = "DOWNLOADING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    TIMEOUT = "TIMEOUT"

    SKIPPED = "SKIPPED"


@dataclass(slots=True)
class DownloadResult:
    """
    Download result model.
    """

    status: DownloadStatus

    success: bool = False

    message: str = ""

    url: str = ""

    filename: str = ""

    output_path: str = ""

    retryable: bool = False

    error: Optional[Exception] = None
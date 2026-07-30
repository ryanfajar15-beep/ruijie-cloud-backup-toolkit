"""
Render Models
Ruijie Cloud Backup Toolkit (RCBT)
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class RenderStatus(str, Enum):
    """Render process status."""

    INIT = "INIT"

    STARTING = "STARTING"

    RUNNING = "RUNNING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    TIMEOUT = "TIMEOUT"

    NETWORK_ERROR = "NETWORK_ERROR"

    UNKNOWN_ERROR = "UNKNOWN_ERROR"


@dataclass(slots=True)
class RenderResult:
    """
    Render result object.
    """

    status: RenderStatus

    success: bool = False

    message: str = ""

    data: Optional[dict[str, Any]] = None

    retryable: bool = False

    error: Optional[Exception] = None

    task_id: str = ""

    scheme_id: str = ""
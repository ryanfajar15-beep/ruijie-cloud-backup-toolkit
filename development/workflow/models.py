"""
Workflow Models
Ruijie Cloud Backup Toolkit (RCBT)
"""

from dataclasses import dataclass
from enum import Enum


class WorkflowStatus(str, Enum):
    """Workflow execution status."""

    PENDING = "PENDING"

    RUNNING = "RUNNING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"

    CANCELLED = "CANCELLED"
    

@dataclass(slots=True)
class WorkflowResult:
    """
    Workflow execution result.
    """

    status: WorkflowStatus

    success: bool = False

    message: str = ""

    retryable: bool = False

    error: Exception | None = None
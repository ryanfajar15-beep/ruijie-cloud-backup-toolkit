"""
Workflow Exceptions
Ruijie Cloud Backup Toolkit (RCBT)
"""


class WorkflowError(Exception):
    """Base workflow exception."""


class WorkflowInitializationError(WorkflowError):
    """Workflow initialization failed."""


class WorkflowExecutionError(WorkflowError):
    """Workflow execution failed."""


class WorkflowValidationError(WorkflowError):
    """Workflow validation failed."""


class WorkflowCancelledError(WorkflowError):
    """Workflow cancelled by user."""
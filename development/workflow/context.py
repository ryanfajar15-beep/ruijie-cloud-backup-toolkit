"""
Workflow Context
Ruijie Cloud Backup Toolkit (RCBT)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from .status import ProjectStatus
from development.workspace.project_writer import ProjectWriter
from development.config.credential import Credential

import requests


@dataclass(slots=True)
class WorkflowContext:
    """
    Shared context across the backup workflow.

    Every workflow step reads from and writes to this object.
    """

    # Workspace
    workspace: Path | None = None

    # HAR selected from incoming/
    selected_har: Path | None = None

    # HAR destination inside workspace
    session_har: Path | None = None

    project_file: Path | None = None

    project_writer: ProjectWriter | None = None

    output_dir: Path | None = None

    backup_file: Path | None = None

    report_dir: Path | None = None

    images_dir: Path | None = None

    images_original_dir: Path | None = None

    images_processed_dir: Path | None = None

    logs_dir: Path | None = None

    # Authentication
    session: requests.Session | None = None

    credential: Credential | None = None

    # Project information
    project_status: ProjectStatus = ProjectStatus.CREATED

    project_name: str = ""

    scheme_id: str = ""

    region_info: dict[str, Any] = field(default_factory=dict)

    # Render
    render_result: dict[str, Any] | None = None

    # Download
    downloaded_files: list[Path] = field(default_factory=list)

    # Report
    report_data: dict[str, Any] = field(default_factory=dict)

    # Metadata
    metadata: dict[str, Any] = field(default_factory=dict)
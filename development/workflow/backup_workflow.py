"""
Backup Workflow
Ruijie Cloud Backup Toolkit (RCBT)

Main orchestration layer.
"""

from __future__ import annotations

from development.workspace.workspace import Workspace
from .status import ProjectStatus
from development.workspace.project_writer import ProjectWriter
from development.workspace.project_info import ProjectInfo

from .context import WorkflowContext
from .models import (
    WorkflowResult,
    WorkflowStatus,
)


class BackupWorkflow:
    """
    Main backup workflow.

    Coordinates all workflow stages.
    """

    def __init__(
        self,
        context: WorkflowContext,
    ):
        self.context = context

    # -------------------------------------------------

    def run(self) -> WorkflowResult:
        """
        Execute backup workflow.
        """

        try:

            self.prepare()

            self.update_status(ProjectStatus.INITIALIZING)

            self.authenticate()

            self.render()

            self.download()

            self.report()

            self.update_status(ProjectStatus.COMPLETED)


            return WorkflowResult(
                status=WorkflowStatus.COMPLETED,
                success=True,
                message="Backup workflow completed successfully.",
            )

        except Exception as exc:

            self.update_status(ProjectStatus.FAILED)

            return WorkflowResult(
                status=WorkflowStatus.FAILED,
                success=False,
                message=str(exc),
                error=exc,
            )

        finally:

            self.cleanup()

    # -------------------------------------------------

    def prepare(self) -> None:
        """
        Prepare workflow resources.
        """

        self.validate_context()

        self.load_project_info()

        workspace = self.create_workspace()

        self.populate_context(workspace)

        self.write_project()
        
    # -------------------------------------------------

    def validate_context(self) -> None:
        """
        Validate workflow context.
        """

        if (
            self.context.selected_har is None
            or not self.context.selected_har.exists()
        ):
            raise ValueError(
                "Selected HAR file does not exist."
            )
        
    # -------------------------------------------------

    def load_project_info(self) -> None:
        """
        Load project metadata from HAR.
        """

        if self.context.selected_har is None:

            raise RuntimeError(
                "HAR file has not been selected."
            )

        info = ProjectInfo(
            self.context.selected_har
        )

        metadata = info.info()

        self.context.metadata = metadata

        self.context.project_name = (
            metadata["project_id"]
        )
        
    # -------------------------------------------------

    def create_workspace(self) -> Workspace:
        """
        Create project workspace.
        """

        workspace = Workspace(
            project_id=self.context.project_name,
        )

        workspace.create()

        return workspace

    # -------------------------------------------------

    def write_project(self) -> None:
        """
        Create initial project.json.
        """

        if self.context.project_writer is None:

            raise RuntimeError(
                "ProjectWriter has not been initialized."
            )

        self.context.project_writer.write(
            self.context.metadata
        )

    # -------------------------------------------------

    def populate_context(
        self,
        workspace: Workspace,
    ) -> None:
        """
        Populate workflow context.
        """

        self.context.workspace = workspace.root

        self.context.session_har = workspace.session_har

        self.context.project_file = workspace.project_file

        self.context.output_dir = workspace.output

        self.context.backup_file = workspace.backup_file

        self.context.report_dir = workspace.report

        self.context.images_dir = workspace.images

        self.context.images_original_dir = (
            workspace.images_original
        )

        self.context.images_processed_dir = (
            workspace.images_processed
        )

        self.context.logs_dir = workspace.logs

        self.context.project_writer = ProjectWriter(
            self.context.project_file
        )

    # -------------------------------------------------
    
    def update_status(
        self,
        status: ProjectStatus,
    ) -> None:
        """
        Update current project status.
        """

        self.context.project_status = status

        if self.context.project_writer:

            self.context.project_writer.update_status(
                status.value
            )

    # -------------------------------------------------

    def authenticate(self) -> None:
        """
        Authentication stage.
        """

        self.update_status(
            ProjectStatus.AUTHENTICATING
        )

        # TODO: Authentication implementation

        pass

    # -------------------------------------------------

    def render(self) -> None:
        """
        Render stage.
        """

        self.update_status(
            ProjectStatus.RENDERING
        )

        # TODO: Render implementation
        pass

    # -------------------------------------------------

    def download(self) -> None:
        """
        Download stage.
        """

        self.update_status(
            ProjectStatus.DOWNLOADING
        )

        # TODO: Download implementation
        pass

    # -------------------------------------------------

    def report(self) -> None:
        """
        Report stage.
        """

        self.update_status(
            ProjectStatus.REPORTING
        )

        # TODO: Report implementation
        pass

    # -------------------------------------------------

    def cleanup(self) -> None:
        """
        Cleanup stage.
        """

        pass
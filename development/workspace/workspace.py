"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Workspace Manager
Phase   : 5.0 - Workspace Flow

Purpose
-------
Mengelola workspace project.

Responsibilities
----------------
✓ Membuat struktur project
✓ Menggunakan PathManager
✓ Menyediakan akses path standar

Tidak melakukan:
✗ Import HAR
✗ Parser
✗ Backup
✗ Report generation

============================================================
"""

from development.workspace.path_manager import (
    PathManager,
)


VERSION = "5.0.0"


class Workspace:

    def __init__(
        self,
        project_id,
        base_dir="projects",
    ):

        self.project_id = project_id

        self.paths = PathManager(
            project_id,
            base_dir,
        )


    # -------------------------------------------------

    @property
    def root(self):

        return self.paths.root


    # -------------------------------------------------

    @property
    def input(self):

        return self.paths.input_dir


    # -------------------------------------------------

    @property
    def output(self):

        return self.paths.output_dir


    # -------------------------------------------------

    @property
    def images(self):

        return self.paths.images_dir


    # -------------------------------------------------

    @property
    def images_original(self):

        return self.paths.images_original


    # -------------------------------------------------

    @property
    def images_processed(self):

        return self.paths.images_processed


    # -------------------------------------------------

    @property
    def report(self):

        return self.paths.report_dir


    # -------------------------------------------------

    @property
    def logs(self):

        return self.paths.logs_dir


    # -------------------------------------------------

    def create(self):
        """
        Create complete workspace structure.
        """

        folders = [

            self.root,

            self.input,

            self.output,

            self.images,

            self.images_original,

            self.images_processed,

            self.report,

            self.logs,

        ]


        for folder in folders:

            folder.mkdir(
                parents=True,
                exist_ok=True,
            )


        return self.root


    # -------------------------------------------------

    @property
    def project_file(self):

        return self.paths.project_file


    # -------------------------------------------------

    @property
    def session_har(self):

        return self.paths.session_har


    # -------------------------------------------------

    @property
    def backup_file(self):

        return self.paths.backup_file


    # -------------------------------------------------

    @property
    def report_pdf(self):

        return self.paths.report_pdf


    # -------------------------------------------------

    @property
    def report_excel(self):

        return self.paths.report_excel


    # -------------------------------------------------

    @property
    def report_html(self):

        return self.paths.report_html
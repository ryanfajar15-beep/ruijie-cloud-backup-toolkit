"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Path Manager
Phase   : 5.0 - Workspace Flow

Purpose
-------
Mengelola seluruh lokasi folder project.

Responsibilities
----------------
✓ Menyediakan path standar workspace
✓ Tidak membuat folder
✓ Tidak menjalankan proses backup
✓ Tidak membaca file

Structure
---------
projects/<project_id>/

├── input/
├── output/
├── images/
│   ├── original/
│   └── processed/
├── report/
└── logs/

============================================================
"""

from pathlib import Path


VERSION = "5.0.0"


class PathManager:

    def __init__(
        self,
        project_id,
        base_dir="projects",
    ):

        self.project_id = project_id

        self.root = (
            Path(base_dir)
            /
            project_id
        )

    # -------------------------------------------------

    @property
    def input_dir(self):

        return self.root / "input"


    # -------------------------------------------------

    @property
    def output_dir(self):

        return self.root / "output"


    # -------------------------------------------------

    @property
    def images_dir(self):

        return self.root / "images"


    # -------------------------------------------------

    @property
    def images_original(self):

        return (
            self.images_dir
            /
            "original"
        )


    # -------------------------------------------------

    @property
    def images_processed(self):

        return (
            self.images_dir
            /
            "processed"
        )


    # -------------------------------------------------

    @property
    def report_dir(self):

        return self.root / "report"


    # -------------------------------------------------

    @property
    def logs_dir(self):

        return self.root / "logs"


    # -------------------------------------------------

    @property
    def session_har(self):

        return (
            self.input_dir
            /
            "session.har"
        )


    # -------------------------------------------------

    @property
    def project_file(self):

        return (
            self.root
            /
            "project.json"
        )


    # -------------------------------------------------

    @property
    def backup_file(self):

        return (
            self.output_dir
            /
            "backup.zip"
        )


    # -------------------------------------------------

    @property
    def report_pdf(self):

        return (
            self.report_dir
            /
            "report.pdf"
        )


    # -------------------------------------------------

    @property
    def report_excel(self):

        return (
            self.report_dir
            /
            "report.xlsx"
        )


    # -------------------------------------------------

    @property
    def report_html(self):

        return (
            self.report_dir
            /
            "report.html"
        )
"""
Workspace Manager
Phase 3.5.1

Mengelola struktur workspace setiap project.
"""

from pathlib import Path


class Workspace:

    def __init__(self, project_name: str):

        self.project_name = project_name

        self.root = Path("projects") / project_name

        self.input = self.root / "input"
        self.output = self.root / "output"
        self.report = self.root / "report"
        self.logs = self.root / "logs"

    # -------------------------------------------------

    def create(self):

        self.root.mkdir(
            parents=True,
            exist_ok=True
        )

        self.input.mkdir(
            parents=True,
            exist_ok=True
        )

        self.output.mkdir(
            parents=True,
            exist_ok=True
        )

        self.report.mkdir(
            parents=True,
            exist_ok=True
        )

        self.logs.mkdir(
            parents=True,
            exist_ok=True
        )

    # -------------------------------------------------

    @property
    def project_file(self):

        return self.root / "project.json"

    @property
    def session_har(self):

        return self.input / "session.har"

    @property
    def request_catalog(self):

        return self.output / "request_catalog.json"

    @property
    def auth_catalog(self):

        return self.output / "auth_catalog.json"

    @property
    def api_catalog(self):

        return self.output / "api_catalog.json"

    @property
    def backup_file(self):

        return self.output / "backup.zip"

    @property
    def report_file(self):

        return self.report / "report.html"

    @property
    def log_file(self):

        return self.logs / "backup.log"
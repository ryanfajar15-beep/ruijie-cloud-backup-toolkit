"""
Path Manager

Mengelola seluruh path project workspace.
"""

from pathlib import Path

from development.workspace.workspace import Workspace


class PathManager:

    def __init__(self, project_name):

        self.workspace = Workspace(project_name)

        self.workspace.create()

    # -------------------------------------------------

    @property
    def root(self):

        return self.workspace.root

    @property
    def input(self):

        return self.workspace.input

    @property
    def output(self):

        return self.workspace.output

    @property
    def report(self):

        return self.workspace.report

    @property
    def logs(self):

        return self.workspace.logs

    # -------------------------------------------------

    @property
    def session_har(self):

        return self.workspace.session_har

    @property
    def project_json(self):

        return self.workspace.project_file

    @property
    def request_catalog(self):

        return self.workspace.request_catalog

    @property
    def auth_catalog(self):

        return self.workspace.auth_catalog

    @property
    def api_catalog(self):

        return self.workspace.api_catalog

    @property
    def backup_file(self):

        return self.workspace.backup_file

    @property
    def report_file(self):

        return self.workspace.report_file

    @property
    def log_file(self):

        return self.workspace.log_file

    # -------------------------------------------------

    def as_dict(self):

        return {

            "root": self.root,

            "input": self.input,

            "output": self.output,

            "report": self.report,

            "logs": self.logs,

            "session_har": self.session_har,

            "project_json": self.project_json,

            "request_catalog": self.request_catalog,

            "auth_catalog": self.auth_catalog,

            "api_catalog": self.api_catalog,

            "backup_file": self.backup_file,

            "report_file": self.report_file,

            "log_file": self.log_file,
        }
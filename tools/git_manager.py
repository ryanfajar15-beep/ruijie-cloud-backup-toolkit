from __future__ import annotations

import subprocess
from pathlib import Path


class GitManager:
    """
    Read Git information for AI Review.
    """

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def _run(self, *args: str) -> str:
        """
        Execute a git command.
        """

        result = subprocess.run(
            ["git", *args],
            cwd=self.project_root,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            return ""

        return result.stdout.strip()

    def current_branch(self) -> str:
        return self._run(
            "branch",
            "--show-current",
        )

    def last_commit(self) -> str:
        return self._run(
            "log",
            "-1",
            "--pretty=%s",
        )

    def modified_files(self) -> list[str]:
        output = self._run(
            "diff",
            "--name-only",
        )

        return [
            line.strip()
            for line in output.splitlines()
            if line.strip()
        ]

    def staged_files(self) -> list[str]:
        output = self._run(
            "diff",
            "--cached",
            "--name-only",
        )

        return [
            line.strip()
            for line in output.splitlines()
            if line.strip()
        ]

    def untracked_files(self) -> list[str]:
        output = self._run(
            "ls-files",
            "--others",
            "--exclude-standard",
        )

        return [
            line.strip()
            for line in output.splitlines()
            if line.strip()
        ]

    def changed_files(self) -> list[str]:
        files = set()

        files.update(self.modified_files())
        files.update(self.staged_files())
        files.update(self.untracked_files())

        return sorted(files)

    def summary(self) -> dict:
        return {
            "branch": self.current_branch(),
            "last_commit": self.last_commit(),
            "changed_files": self.changed_files(),
        }
from __future__ import annotations

from pathlib import Path
import yaml


class StateManager:
    """
    Read AI State from .ai/state/state.yaml
    """

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.state_file = (
            project_root
            / ".ai"
            / "state"
            / "state.yaml"
        )

    def load(self) -> dict:
        if not self.state_file.exists():
            raise FileNotFoundError(
                f"State file not found: {self.state_file}"
            )

        with self.state_file.open(
            "r",
            encoding="utf-8",
        ) as fp:
            return yaml.safe_load(fp) or {}
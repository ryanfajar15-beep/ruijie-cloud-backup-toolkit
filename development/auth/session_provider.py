"""
RCBT Session Provider

Load browser session cookie.
"""

from __future__ import annotations

import json
from pathlib import Path


class SessionProvider:
    """
    Provides authenticated cookies.
    """

    def __init__(
        self,
        session_file: str = "config/session.json",
    ):
        self.session_file = Path(session_file)


    def load(self) -> dict:
        """
        Load cookies from json file.
        """

        if not self.session_file.exists():
            raise FileNotFoundError(
                f"Session file not found: {self.session_file}"
            )


        with self.session_file.open(
            "r",
            encoding="utf-8",
        ) as f:
            data = json.load(f)


        return data.get(
            "cookies",
            {}
        )
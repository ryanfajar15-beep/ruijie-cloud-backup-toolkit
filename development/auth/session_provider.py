"""
RCBT Session Provider

Responsible for managing a single requests.Session instance
used by the authentication layer.
"""

from __future__ import annotations

import json
from pathlib import Path

import requests


class SessionProvider:
    """
    Provide and maintain a shared requests.Session.
    """

    def __init__(
        self,
        session_file: str = "config/session.json",
    ) -> None:

        self._session_file = Path(session_file)
        self._session = requests.Session()

    @property
    def session(self) -> requests.Session:
        """
        Return active requests session.
        """
        return self._session

    def load(self) -> requests.Session:
        """
        Load cookies from session file.
        """

        if not self._session_file.exists():
            return self._session

        with self._session_file.open(
            "r",
            encoding="utf-8",
        ) as fp:
            data = json.load(fp)

        cookies = data.get("cookies", {})

        self._session.cookies.update(cookies)

        return self._session

    def save(self) -> None:
        """
        Save current cookies.
        """

        self._session_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        data = {
            "cookies": requests.utils.dict_from_cookiejar(
                self._session.cookies
            )
        }

        with self._session_file.open(
            "w",
            encoding="utf-8",
        ) as fp:
            json.dump(
                data,
                fp,
                indent=4,
            )

    def clear(self) -> None:
        """
        Clear current session cookies.
        """

        self._session.cookies.clear()
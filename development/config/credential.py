"""
Credential Model
Ruijie Cloud Backup Toolkit (RCBT)
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Credential:
    """
    User credential.
    """

    username: str
    password: str
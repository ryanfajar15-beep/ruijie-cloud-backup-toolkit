"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Parser Package

Public Interface
----------------
Expose parser engine versi aktif.

Phase
-----
6.0 - Workspace Integration

============================================================
"""


from development.parser.versions.parser_v05 import (
    HarParser,
)


VERSION = "0.5.0"


__all__ = [
    "HarParser",
]
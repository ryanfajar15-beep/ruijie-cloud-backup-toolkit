"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Parser Package
Version : 0.4.0

Public Interface
----------------
Expose parser engine tanpa bergantung
ke versi implementasi.

============================================================
"""

from development.parser.versions.parser_v04 import (
    HarParser,
)


VERSION = "0.4.0"


__all__ = [
    "HarParser",
]
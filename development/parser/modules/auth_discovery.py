"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Authentication Discovery
Version : 0.4.0
Phase   : 4.1 - Authentication Discovery

Purpose
-------
Mendeteksi informasi authentication dari request HAR.

Responsibilities
----------------
✓ Extract headers
✓ Extract cookies
✓ Extract authorization token
✓ Return authentication catalog

Tidak melakukan:
✗ File output
✗ Workspace management
✗ API processing

============================================================
"""

from collections import defaultdict


VERSION = "0.4.0"


def discover_auth(
    requests: list,
) -> dict:
    """
    Discover authentication data.

    Parameters
    ----------
    requests : list
        Normalized request objects.

    Returns
    -------
    dict
        Authentication catalog.
    """

    result = {
        "headers": defaultdict(set),
        "cookies": set(),
        "authorization": set(),
    }

    for request in requests:

        for header in request.get(
            "headers",
            [],
        ):

            name = header.get(
                "name",
                "",
            )

            value = header.get(
                "value",
                "",
            )

            if not name:
                continue

            result["headers"][name].add(
                value
            )

            lower_name = name.lower()

            if lower_name == "authorization":
                result["authorization"].add(
                    value
                )

            if lower_name == "cookie":
                result["cookies"].add(
                    value
                )

    return {
        "headers": {
            key: sorted(list(values))
            for key, values in result["headers"].items()
        },

        "cookies": sorted(
            list(result["cookies"])
        ),

        "authorization": sorted(
            list(result["authorization"])
        ),
    }
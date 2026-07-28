"""
Authentication Discovery
Phase 4.1

Menemukan Header, Cookie, dan Authorization
dari seluruh request HAR.
"""

from collections import defaultdict


def discover_auth(requests):
    """
    Mencari informasi authentication dari request.
    """

    result = {
        "headers": defaultdict(set),
        "cookies": set(),
        "authorization": set(),
    }

    for request in requests:

        # -----------------------------
        # Headers
        # -----------------------------
        for header in request.get("headers", []):

            name = header.get("name", "")
            value = header.get("value", "")

            if not name:
                continue

            result["headers"][name].add(value)

            if name.lower() == "authorization":
                result["authorization"].add(value)

            if name.lower() == "cookie":
                result["cookies"].add(value)

    return {
        "headers": {
            k: sorted(list(v))
            for k, v in result["headers"].items()
        },
        "cookies": sorted(list(result["cookies"])),
        "authorization": sorted(list(result["authorization"])),
    }
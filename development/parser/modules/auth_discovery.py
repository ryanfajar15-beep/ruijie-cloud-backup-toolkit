"""
============================================================
Ruijie Cloud Backup Toolkit (RCBT)

Module  : Authentication Discovery
Version : 0.5.0
Phase   : 6.1 - Authentication Catalog

Purpose
-------
Mendeteksi informasi authentication
dari request HAR.

Responsibilities
----------------
✓ Extract headers
✓ Extract cookies
✓ Extract authorization token
✓ Extract bearer token
✓ Extract csrf token
✓ Extract session identifier

Tidak melakukan:
✗ File output
✗ Workspace management
✗ API processing

============================================================
"""

from collections import defaultdict


VERSION = "0.5.0"



AUTH_HEADER_NAMES = {

    "authorization",

    "cookie",

    "x-csrf-token",

    "csrf-token",

    "x-auth-token",

    "token",

    "session",

    "set-cookie",

}



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

        "version": VERSION,

        "headers": defaultdict(set),

        "cookies": set(),

        "authorization": set(),

        "tokens": set(),

        "csrf": set(),

        "sessions": set(),

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


            if not name or not value:

                continue



            lower_name = (
                name
                .lower()
                .strip()
            )


            # Store selected headers

            if lower_name in AUTH_HEADER_NAMES:

                result["headers"][name].add(
                    value
                )



            # Authorization

            if lower_name == "authorization":

                result["authorization"].add(
                    value
                )


                if (
                    "bearer "
                    in value.lower()
                ):

                    result["tokens"].add(
                        value
                    )



            # Cookie

            if lower_name == "cookie":

                result["cookies"].add(
                    value
                )



            # CSRF

            if (
                "csrf"
                in lower_name
            ):

                result["csrf"].add(
                    value
                )



            # Session

            if (
                "session"
                in lower_name
            ):

                result["sessions"].add(
                    value
                )



    return {


        "version": VERSION,


        "headers": {

            key: sorted(
                list(values)
            )

            for key, values
            in result["headers"].items()

        },


        "cookies": sorted(
            list(
                result["cookies"]
            )
        ),


        "authorization": sorted(
            list(
                result["authorization"]
            )
        ),


        "tokens": sorted(
            list(
                result["tokens"]
            )
        ),


        "csrf": sorted(
            list(
                result["csrf"]
            )
        ),


        "sessions": sorted(
            list(
                result["sessions"]
            )
        ),

    }

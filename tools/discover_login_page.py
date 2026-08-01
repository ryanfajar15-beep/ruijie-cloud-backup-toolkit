from pathlib import Path
import re

from utils import load_json, save_json, print_title


INPUT_FILE = Path(
    "analysis/api_analysis_requests.json"
)

OUTPUT_FILE = Path(
    "analysis/auth/login_metadata.json"
)


LOGIN_PATTERN = "/sso/login"


HIDDEN_FIELDS = [
    "lt",
    "execution",
    "sign",
    "_eventId",
]


LOGIN_FIELDS = [
    "username",
    "password",
    "selectedCloud",
    "googleTotpCode",
    "disposableCode",
]


def extract_query_params(url):

    params = {}

    if "?" not in url:
        return params

    query = url.split("?", 1)[1]

    for item in query.split("&"):

        if "=" in item:

            key, value = item.split(
                "=",
                1
            )

            params[key] = value

    return params


def discover_login_page():

    requests = load_json(
        INPUT_FILE
    )

    login_entries = []

    for req in requests:

        url = req.get(
            "url",
            ""
        )

        if LOGIN_PATTERN not in url:
            continue

        entry = {

            "url": url,

            "method": req.get(
                "method"
            ),

            "query_params": extract_query_params(
                url
            ),

            "post_data": {},

            "fields_found": [],

        }

        post = req.get(
            "postData"
        ) or {}

        text = post.get(
            "text",
            ""
        )

        if text:

            fields = re.findall(
                r"([a-zA-Z0-9_]+)=",
                text
            )

            entry["fields_found"] = sorted(
                set(fields)
            )

            entry["post_data"] = {
                "mimeType": post.get(
                    "mimeType"
                )
            }


        login_entries.append(
            entry
        )


    hidden_found = set()

    form_found = set()


    for entry in login_entries:

        for field in entry.get(
            "fields_found",
            []
        ):

            if field in HIDDEN_FIELDS:
                hidden_found.add(
                    field
                )

            if field in LOGIN_FIELDS:
                form_found.add(
                    field
                )


    result = {

        "login_page": {

            "endpoint": LOGIN_PATTERN,

            "total_requests": len(
                login_entries
            ),

            "hidden_fields": sorted(
                hidden_found
            ),

            "form_fields": sorted(
                form_found
            ),

        },

        "requests": login_entries,

    }


    save_json(
        OUTPUT_FILE,
        result
    )


    print_title(
        "LOGIN PAGE DISCOVERY"
    )

    print(
        f"TOTAL LOGIN REQUEST : {len(login_entries)}"
    )

    print(
        "HIDDEN FIELDS"
    )

    for item in sorted(hidden_found):

        print(
            f"- {item}"
        )


    print(
        "\nFORM FIELDS"
    )

    for item in sorted(form_found):

        print(
            f"- {item}"
        )


    print(
        "\nOUTPUT"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    discover_login_page()
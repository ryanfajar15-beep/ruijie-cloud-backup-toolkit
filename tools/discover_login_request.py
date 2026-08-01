from pathlib import Path
import urllib.parse

from utils import load_json, save_json, print_title


INPUT_FILE = Path(
    "analysis/api_analysis_requests.json"
)

OUTPUT_FILE = Path(
    "analysis/auth/login_request_metadata.json"
)


LOGIN_ENDPOINT = "/sso/login"


EXPECTED_FIELDS = {
    "username",
    "password",
    "lt",
    "execution",
    "sign",
    "_eventId",
    "selectedCloud",
    "googleTotpCode",
    "disposableCode",
}


def parse_form_data(text):

    data = {}

    if not text:
        return data

    for item in text.split("&"):

        if "=" not in item:
            continue

        key, value = item.split(
            "=",
            1
        )

        data[key] = urllib.parse.unquote(
            value
        )

    return data


def discover_login_request():

    requests = load_json(
        INPUT_FILE
    )

    login_requests = []


    for req in requests:

        url = req.get(
            "url",
            ""
        )

        method = req.get(
            "method"
        )

        if (
            LOGIN_ENDPOINT not in url
            or method != "POST"
        ):
            continue


        post = req.get(
            "postData"
        ) or {}


        text = post.get(
            "text",
            ""
        )


        payload = parse_form_data(
            text
        )


        login_requests.append(
            {
                "url": url,
                "method": method,
                "mimeType": post.get(
                    "mimeType"
                ),
                "fields": sorted(
                    payload.keys()
                ),
                "payload": payload,
            }
        )


    discovered_fields = set()


    for item in login_requests:

        discovered_fields.update(
            item.get(
                "fields",
                []
            )
        )


    result = {

        "login_request": {

            "endpoint": LOGIN_ENDPOINT,

            "method": "POST",

            "total_requests": len(
                login_requests
            ),

            "required_fields": sorted(
                discovered_fields.intersection(
                    EXPECTED_FIELDS
                )
            ),

            "all_fields": sorted(
                discovered_fields
            ),

        },

        "requests": login_requests,

    }


    save_json(
        OUTPUT_FILE,
        result
    )


    print_title(
        "LOGIN REQUEST DISCOVERY"
    )


    print(
        f"TOTAL LOGIN POST : {len(login_requests)}"
    )


    print(
        "FIELDS"
    )

    for field in sorted(discovered_fields):

        print(
            f"- {field}"
        )


    print(
        "\nOUTPUT"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    discover_login_request()
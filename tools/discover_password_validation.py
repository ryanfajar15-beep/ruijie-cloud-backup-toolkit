from pathlib import Path
import json

from utils import load_json, save_json, print_title


INPUT_FILE = Path(
    "analysis/api_analysis_requests.json"
)

OUTPUT_FILE = Path(
    "analysis/auth/password_validation_metadata.json"
)


VALIDATE_ENDPOINT = "/sso/validate/password"


def extract_payload(req):

    post = req.get(
        "postData"
    ) or {}

    text = post.get(
        "text",
        ""
    )

    if not text:
        return {}

    try:
        return json.loads(text)

    except Exception:
        return {
            "raw": text
        }


def discover_password_validation():

    requests = load_json(
        INPUT_FILE
    )

    validation_requests = []

    for req in requests:

        url = req.get(
            "url",
            ""
        )

        if VALIDATE_ENDPOINT not in url:
            continue


        payload = extract_payload(
            req
        )


        validation_requests.append(
            {
                "url": url,
                "method": req.get(
                    "method"
                ),
                "payload": payload,
            }
        )


    fields = set()

    samples = {}


    for item in validation_requests:

        payload = item.get(
            "payload",
            {}
        )

        if not isinstance(payload, dict):
            continue


        for key, value in payload.items():

            fields.add(
                key
            )

            if key not in samples:

                samples[key] = {

                    "sample": value,

                    "type": type(value).__name__

                }


    result = {

        "password_validation": {

            "endpoint": VALIDATE_ENDPOINT,

            "total_requests": len(
                validation_requests
            ),

            "payload_fields": sorted(
                fields
            ),

            "field_metadata": samples,

        },

        "requests": validation_requests,

    }


    save_json(
        OUTPUT_FILE,
        result
    )


    print_title(
        "PASSWORD VALIDATION DISCOVERY"
    )


    print(
        f"TOTAL REQUESTS : {len(validation_requests)}"
    )


    print(
        "PAYLOAD FIELDS"
    )


    for field in sorted(fields):

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

    discover_password_validation()
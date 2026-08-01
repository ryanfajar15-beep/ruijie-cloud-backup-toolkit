from pathlib import Path
import json
import re

from utils import load_json, save_json, print_title


INPUT_FILE = Path(
    "analysis/api_analysis_requests.json"
)

OUTPUT_FILE = Path(
    "analysis/auth/rsa_metadata.json"
)


RSA_ENDPOINTS = [
    "/sso/validate/password",
]


def find_rsa_requests(requests):

    results = []

    for req in requests:

        url = req.get(
            "url",
            ""
        )

        if any(
            endpoint in url
            for endpoint in RSA_ENDPOINTS
        ):

            results.append(req)

    return results


def extract_payload(req):

    post_data = req.get(
        "postData"
    ) or {}

    text = post_data.get(
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


def detect_encrypted_field(payload):

    fields = []

    if isinstance(payload, dict):

        for key, value in payload.items():

            if not isinstance(value, str):
                continue

            #
            # encrypted password usually
            # has long base64/hex string
            #

            if len(value) > 50:

                fields.append(
                    {
                        "field": key,
                        "length": len(value),
                        "sample": value[:20] + "..."
                    }
                )

    return fields


def discover_rsa_metadata():

    requests = load_json(
        INPUT_FILE
    )

    rsa_requests = find_rsa_requests(
        requests
    )


    payloads = []

    encrypted_fields = []


    for req in rsa_requests:

        payload = extract_payload(
            req
        )

        payloads.append(
            payload
        )

        encrypted_fields.extend(
            detect_encrypted_field(
                payload
            )
        )


    result = {

        "rsa": {

            "endpoint": "/sso/validate/password",

            "algorithm": "RSA",

            "requests_found": len(
                rsa_requests
            ),

            "encrypted_fields": encrypted_fields,

        },

        "payload_samples": payloads,

    }


    save_json(
        OUTPUT_FILE,
        result
    )


    print_title(
        "RSA METADATA DISCOVERY"
    )

    print(
        f"RSA REQUESTS : {len(rsa_requests)}"
    )

    print(
        "ENCRYPTED FIELDS"
    )

    for item in encrypted_fields:

        print(
            f"- {item['field']} "
            f"({item['length']} chars)"
        )


    print(
        "\nOUTPUT"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    discover_rsa_metadata()
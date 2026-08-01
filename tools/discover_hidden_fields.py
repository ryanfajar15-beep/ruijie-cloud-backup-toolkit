from pathlib import Path

from utils import load_json, save_json, print_title


INPUT_FILE = Path(
    "analysis/api_analysis_requests.json"
)

OUTPUT_FILE = Path(
    "analysis/auth/hidden_fields_metadata.json"
)


LOGIN_ENDPOINT = "/sso/login"


KNOWN_HIDDEN_FIELDS = {
    "lt",
    "execution",
    "sign",
    "_eventId",
}


def discover_hidden_fields():

    requests = load_json(
        INPUT_FILE
    )

    fields = {}


    for req in requests:

        url = req.get(
            "url",
            ""
        )

        if LOGIN_ENDPOINT not in url:
            continue


        post = req.get(
            "postData"
        ) or {}


        text = post.get(
            "text",
            ""
        )


        if not text:
            continue


        #
        # Parse x-www-form-urlencoded
        #

        for item in text.split("&"):

            if "=" not in item:
                continue


            key, value = item.split(
                "=",
                1
            )


            if key not in KNOWN_HIDDEN_FIELDS:
                continue


            if key not in fields:

                fields[key] = {

                    "field": key,

                    "samples": [],

                    "lengths": [],

                }


            if value not in fields[key]["samples"]:

                fields[key]["samples"].append(
                    value
                )


            fields[key]["lengths"].append(
                len(value)
            )


    result = {

        "hidden_fields": list(
            fields.values()
        ),

        "total_fields": len(
            fields
        ),

    }


    save_json(
        OUTPUT_FILE,
        result
    )


    print_title(
        "HIDDEN FIELD DISCOVERY"
    )


    print(
        f"TOTAL HIDDEN FIELDS : {len(fields)}"
    )


    for field in fields.values():

        print(
            f"- {field['field']} "
            f"samples={len(field['samples'])}"
        )


    print(
        "\nOUTPUT"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    discover_hidden_fields()
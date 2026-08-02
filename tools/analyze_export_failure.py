from pathlib import Path
import json
from datetime import datetime, timezone


INPUT_FILE = Path(
    "input/cloud-as.ruijienetworks.com_New_300726_00.10.har"
)

OUTPUT_FILE = Path(
    "analysis/workflow/export_failure_metadata.json"
)

LAST_POLL_FILE = Path(
    "analysis/workflow/export_failure_last_poll.json"
)


TARGET_API = [
    "/plan/render/async/start",
    "/plan/render/async/result"
]


ERROR_KEYWORDS = [
    "error",
    "failed",
    "fail",
    "timeout",
    "exception"
]


SUCCESS_KEYWORDS = [
    "success",
    "completed",
    "finish",
    "done"
]


ARTIFACT_KEYWORDS = [
    "download",
    "file",
    "zip",
    "xlsx",
    "csv",
    "pdf",
    "cos",
    "url"
]


def load_har():

    with INPUT_FILE.open() as f:
        return json.load(f)


def extract_body(entry):

    content = (
        entry
        .get("response", {})
        .get("content", {})
    )

    return content.get(
        "text",
        ""
    ) or ""


def compact_body(text):

    return {
        "length": len(text),
        "preview": text[:500]
    }


def analyze():

    har = load_har()

    start_count = 0
    poll_count = 0

    errors = []
    success = []

    artifact_candidates = []

    last_poll = None


    for entry in har["log"]["entries"]:

        url = (
            entry
            .get("request", {})
            .get("url", "")
        )


        api = None

        for target in TARGET_API:

            if target in url:
                api = target
                break


        if not api:
            continue


        body = extract_body(entry)

        body_lower = body.lower()


        item = {

            "time":
                entry.get(
                    "startedDateTime"
                ),

            "api":
                api,

            "status":
                entry.get(
                    "response",
                    {}
                ).get(
                    "status"
                ),

            "body":
                compact_body(
                    body
                )
        }


        if api.endswith(
            "/start"
        ):

            start_count += 1


        if api.endswith(
            "/result"
        ):

            poll_count += 1

            last_poll = item


        if any(
            key in body_lower
            for key in ERROR_KEYWORDS
        ):

            errors.append(
                item
            )


        if any(
            key in body_lower
            for key in SUCCESS_KEYWORDS
        ):

            success.append(
                item
            )


        if any(
            key in body_lower
            for key in ARTIFACT_KEYWORDS
        ):

            artifact_candidates.append(
                item
            )


    return {

        "start_count":
            start_count,

        "poll_count":
            poll_count,

        "last_poll":
            last_poll,

        "error_count":
            len(errors),

        "errors":
            errors[-10:],

        "success_count":
            len(success),

        "artifact_candidate_count":
            len(artifact_candidates),

        "artifact_candidates":
            artifact_candidates[-10:]
    }


def main():

    print("=" * 80)
    print("EXPORT FAILURE ANALYSIS")
    print("=" * 80)


    analysis = analyze()


    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    if analysis["last_poll"]:

        LAST_POLL_FILE.write_text(
            json.dumps(
                analysis["last_poll"],
                indent=2
            )
        )


    output = {

        "metadata": {

            "generated_by":
                "RCBT Workflow Analysis Engine",

            "generated_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        },

        "workflow":
            "export_failure_analysis",

        "analysis": {

            "start_count":
                analysis["start_count"],

            "poll_count":
                analysis["poll_count"],

            "error_count":
                analysis["error_count"],

            "success_count":
                analysis["success_count"],

            "artifact_candidate_count":
                analysis["artifact_candidate_count"],

            "last_poll_file":
                str(
                    LAST_POLL_FILE
                ),

            "errors":
                analysis["errors"],

            "artifact_candidates":
                analysis["artifact_candidates"]
        }
    }


    OUTPUT_FILE.write_text(
        json.dumps(
            output,
            indent=2
        )
    )


    print(
        f"START REQUEST : {analysis['start_count']}"
    )

    print(
        f"POLL REQUEST  : {analysis['poll_count']}"
    )

    print(
        f"ERROR FOUND   : {analysis['error_count']}"
    )

    print(
        f"SUCCESS FOUND : {analysis['success_count']}"
    )

    print(
        f"ARTIFACT CANDIDATE : {analysis['artifact_candidate_count']}"
    )

    print()
    print("OUTPUT")
    print(OUTPUT_FILE)

    if analysis["last_poll"]:

        print(
            "LAST POLL"
        )

        print(
            LAST_POLL_FILE
        )


if __name__ == "__main__":
    main()
from pathlib import Path
import json


def load_json(path):
    """
    Load JSON file.
    """
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    """
    Save JSON file.
    """
    path = Path(path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with path.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False,
        )


def print_title(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)
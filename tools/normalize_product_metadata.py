#!/usr/bin/env python3
"""
==============================================================================
RCBT - Product Metadata Normalizer
==============================================================================

Input
-----
analysis/product/product_metadata.json

Rules
-----
analysis/product/product_normalization.json

Output
------
analysis/product/product_metadata_normalized.json
"""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "analysis/product/product_metadata.json"
RULE_FILE = PROJECT_ROOT / "analysis/product/product_normalization.json"
OUTPUT_FILE = PROJECT_ROOT / "analysis/product/product_metadata_normalized.json"


def load_json(path: Path):

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def apply_rules(record: dict, rules: list) -> dict:
    """
    Normalize product metadata.

    Backward compatible:
    - product_model tetap dipertahankan (original)
    - normalized_product ditambahkan sebagai hasil normalisasi
    """

    result = dict(record)

    original_model = str(
        result.get("product_model", "")
    ).strip()

    result["normalized_product"] = original_model

    for rule in rules:

        matched = True

        for key, value in rule.get("match", {}).items():

            if str(result.get(key, "")).strip() != str(value).strip():
                matched = False
                break

        if not matched:
            continue

        replace = dict(rule.get("replace", {}))

        # Jangan overwrite product_model.
        # Simpan hasil normalisasi pada field baru.
        if "product_model" in replace:

            result["normalized_product"] = str(
                replace["product_model"]
            ).strip()

            del replace["product_model"]

        result.update(replace)

    return result


def main():

    if not INPUT_FILE.exists():
        raise FileNotFoundError(INPUT_FILE)

    if not RULE_FILE.exists():
        raise FileNotFoundError(RULE_FILE)

    metadata = load_json(INPUT_FILE)

    rule_data = load_json(RULE_FILE)

    rules = rule_data.get("rules", [])

    normalized = []

    for item in metadata:

        normalized.append(
            apply_rules(
                item,
                rules,
            )
        )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            normalized,
            f,
            indent=4,
            ensure_ascii=False,
        )

    print("=" * 60)
    print(f"Products : {len(normalized)}")
    print(f"Rules    : {len(rules)}")
    print(f"Output   : {OUTPUT_FILE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
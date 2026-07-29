#!/usr/bin/env python3
"""
Ruijie Cloud Backup Toolkit (RCBT)

AI Review Controller
"""

from __future__ import annotations

import sys
from pathlib import Path

from context_manager import ContextManager
from git_manager import GitManager
from report_builder import ReportBuilder
from state_manager import StateManager

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def banner() -> None:
    """Display CLI banner."""

    print("=" * 60)
    print("RCBT AI REVIEW")
    print("=" * 60)
    print(f"Project Root : {PROJECT_ROOT}")
    print()


def main() -> int:
    """Application entry point."""

    banner()

    # ==========================================================
    # 1. Load AI State
    # ==========================================================

    print("[1/5] Loading AI State...")

    state = StateManager(PROJECT_ROOT).load()

    current = state.get("current", {})

    print(f"Phase  : {current.get('phase', '-')}")
    print(f"Module : {current.get('module', '-')}")
    print(f"Task   : {current.get('task', '-')}")

    print()

    # ==========================================================
    # 2. Load Project Context
    # ==========================================================

    print("[2/5] Loading Project Context...")

    context = ContextManager(PROJECT_ROOT)
    documents = context.load_all()

    print(f"Loaded {len(documents)} context document(s).")

    print()

    # ==========================================================
    # 3. Collect Git Information
    # ==========================================================

    print("[3/5] Collecting Git Information...")

    git = GitManager(PROJECT_ROOT)
    summary = git.summary()

    print(f"Branch      : {summary['branch']}")
    print(f"Last Commit : {summary['last_commit']}")

    print()

    print("Changed Files")

    if summary["changed_files"]:
        for file in summary["changed_files"]:
            print(f" - {file}")
    else:
        print(" - None")

    print()

    # ==========================================================
    # 4. Build Review Context
    # ==========================================================

    print("[4/5] Building Review Context...")

    print("Context successfully built.")

    print()

    # ==========================================================
    # 5. Export Report
    # ==========================================================

    print("[5/5] Exporting Review Report...")

    builder = ReportBuilder(PROJECT_ROOT)

    report = builder.write(
        state=state,
        documents=documents,
        git_summary=summary,
    )

    print(f"Report : {report}")

    print()

    print("=" * 60)
    print("RCBT REVIEW SUMMARY")
    print("=" * 60)

    print(f"Phase        : {current.get('phase', '-')}")
    print(f"Module       : {current.get('module', '-')}")
    print(f"Task         : {current.get('task', '-')}")

    print()

    print(f"Branch       : {summary['branch']}")
    print(f"Last Commit  : {summary['last_commit']}")

    print()

    print(f"Changed Files : {len(summary['changed_files'])}")
    print(f"Context Docs  : {len(documents)}")

    print()
    print("Review workflow completed.")
    print(f"Report saved to: {report}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
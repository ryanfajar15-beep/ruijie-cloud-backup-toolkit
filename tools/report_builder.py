from __future__ import annotations

from pathlib import Path


class ReportBuilder:
    """
    Build AI review report.
    """

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.output_dir = project_root / ".ai" / "review"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write(
        self,
        state: dict,
        documents: dict[str, str],
        git_summary: dict,
    ) -> Path:
        """
        Generate review report.
        """

        report_file = self.output_dir / "report.md"

        current = state.get("current", {})

        lines: list[str] = []

        lines.append("# RCBT AI Review Report")
        lines.append("")

        lines.append("## Project")
        lines.append("Ruijie Cloud Backup Toolkit")
        lines.append("")

        lines.append("## Current State")
        lines.append(f"- Phase: {current.get('phase', '-')}")
        lines.append(f"- Module: {current.get('module', '-')}")
        lines.append(f"- Task: {current.get('task', '-')}")
        lines.append("")

        lines.append("## Git")
        lines.append(f"- Branch: {git_summary.get('branch', '-')}")
        lines.append(f"- Last Commit: {git_summary.get('last_commit', '-')}")
        lines.append("")

        lines.append("## Changed Files")

        changed_files = git_summary.get("changed_files", [])

        if changed_files:
            for file in changed_files:
                lines.append(f"- {file}")
        else:
            lines.append("- None")

        lines.append("")

        lines.append("## Context Documents")

        if documents:
            for document in sorted(documents.keys()):
                lines.append(f"- {document}")
        else:
            lines.append("- None")

        lines.append("")

        lines.append("## Review Status")
        lines.append("READY")
        lines.append("")

        report_file.write_text(
            "\n".join(lines),
            encoding="utf-8",
        )

        return report_file
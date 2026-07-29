from __future__ import annotations

from pathlib import Path


class ContextManager:
    """
    Load project documentation from docs/.
    """

    def __init__(self, project_root: Path):
        self.docs_dir = project_root / "docs"

    def read(self, filename: str) -> str:
        path = self.docs_dir / filename

        if not path.exists():
            raise FileNotFoundError(f"Document not found: {path}")

        return path.read_text(encoding="utf-8")

    def load_all(self) -> dict[str, str]:
        documents = {}

        for file in sorted(self.docs_dir.glob("*.md")):
            documents[file.name] = file.read_text(encoding="utf-8")

        return documents
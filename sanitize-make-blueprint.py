#!/usr/bin/env python3
"""
Sanitize Make blueprint JSON for public sharing.
Usage:
  python sanitize-make-blueprint.py "path/to/blueprint.json" [--backup]

This script replaces connection identifiers, account labels, and common
resource IDs while preserving the blueprint structure and mappings.
"""

import argparse
import json
import re
from pathlib import Path


OPAQUE_VALUE_PATTERNS = [
    re.compile(r"^[A-Za-z0-9_-]{16,}$"),
    re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"),
]

EXACT_KEY_PLACEHOLDERS = {
    "__IMTCONN__": 0,
    "base": "BASE_PLACEHOLDER",
    "table": "TABLE_PLACEHOLDER",
    "spreadsheetId": "SPREADSHEET_PLACEHOLDER",
    "folderId": "FOLDER_PLACEHOLDER",
    "channel": "CHANNEL_PLACEHOLDER",
}

EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.\w+")


def looks_opaque(value: str) -> bool:
    return any(pattern.match(value) for pattern in OPAQUE_VALUE_PATTERNS)


def sanitize_string(key: str, value: str):
    if value.startswith("{{") or value.startswith("}}"):
        return value

    if key in EXACT_KEY_PLACEHOLDERS:
        return EXACT_KEY_PLACEHOLDERS[key]

    if key == "connection":
        return "CONNECTION_PLACEHOLDER"

    if key == "label" and EMAIL_RE.search(value):
        return EMAIL_RE.sub("user@example.com", value)

    if key == "label" and "connection" in value.lower():
        return "Placeholder connection"

    if key == "path" and isinstance(value, str) and value.startswith("/"):
        return "/PLACEHOLDER"

    if key.lower().endswith("id"):
        if looks_opaque(value) or len(value) >= 8:
            return f"{key.upper()}_PLACEHOLDER"

    if looks_opaque(value):
        return "SECRET_PLACEHOLDER"

    return value


def sanitize(obj, parent_key=""):
    if isinstance(obj, dict):
        new = {}
        for key, value in obj.items():
            if key in EXACT_KEY_PLACEHOLDERS:
                new[key] = EXACT_KEY_PLACEHOLDERS[key]
                continue

            if key == "connection" and isinstance(value, str):
                new[key] = "CONNECTION_PLACEHOLDER"
                continue

            if key == "label" and isinstance(value, str):
                new[key] = sanitize_string(key, value)
                continue

            if isinstance(value, str):
                new[key] = sanitize_string(key, value)
            elif isinstance(value, list):
                new[key] = [sanitize(item, key) for item in value]
            else:
                new[key] = sanitize(value, key)
        return new

    if isinstance(obj, list):
        return [sanitize(item, parent_key) for item in obj]

    if isinstance(obj, (int, float, bool, type(None))):
        if parent_key == "__IMTCONN__":
            return 0
        return obj

    return obj


def main():
    parser = argparse.ArgumentParser(description="Sanitize Make blueprint JSON for public sharing")
    parser.add_argument("input", help="Input JSON file path")
    parser.add_argument("--backup", action="store_true", help="Keep a backup file with .bak suffix")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    sanitized = sanitize(data)

    if args.backup:
        backup = path.with_suffix(path.suffix + ".bak")
        backup.write_text(raw, encoding="utf-8")
        print(f"Backup written to {backup}")

    path.write_text(json.dumps(sanitized, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Sanitized JSON written to {path}")


if __name__ == "__main__":
    main()

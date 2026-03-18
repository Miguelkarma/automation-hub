#!/usr/bin/env python3
"""
Sanitize n8n workflow JSON for public sharing.
Usage:
  python sanitize_n8n_flow.py "path/to/flow.json" [--backup]

This script replaces sensitive IDs, webhook IDs, and credentials with placeholders.
It preserves node structure and logic.
"""

import argparse
import json
import re
from pathlib import Path

# Some keys that often contain secrets
SENSITIVE_KEY_EXACT = {
    "formId": "FORM_PLACEHOLDER",
    "webhookId": "WEBHOOK_PLACEHOLDER",
    "instanceId": "INSTANCE_PLACEHOLDER",
    "versionId": "VERSION_PLACEHOLDER",
    "token": "TOKEN_PLACEHOLDER",
    "apiKey": "API_KEY_PLACEHOLDER",
}

SENSITIVE_VALUE_PATTERNS = [
    re.compile(r"^[A-Za-z0-9_\-]{16,}$"),
    re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"),
]

CREDENTIAL_NAME_PLACEHOLDER = "Placeholder Credential"

def sanitize_value(key, value):
    # Keep numbers, booleans, None
    if isinstance(value, (int, float, bool, type(None))):
        return value
    if isinstance(value, str):
        # Replace exact sensitive keys by value if key known
        if key in SENSITIVE_KEY_EXACT:
            return SENSITIVE_KEY_EXACT[key]

        # Replace credential placeholder strings
        if any(sub in key.lower() for sub in ["apikey", "api_key", "token", "secret", "id"]):
            # For known keys, replace long opaque values
            if len(value) >= 8 and any(p.match(value) for p in SENSITIVE_VALUE_PATTERNS):
                return f"{key.upper()}_PLACEHOLDER"

        # For values that look like UUID/webhook ids etc
        if any(p.match(value) for p in SENSITIVE_VALUE_PATTERNS):
            # Avoid replacing obvious plain text labels or templates
            if not value.startswith("={{") and not value.startswith("models/"):
                return "SECRET_PLACEHOLDER"

    return value


def sanitize(obj):
    if isinstance(obj, dict):
        new = {}
        for k, v in obj.items():
            new_key = k
            # sanitize key names for specific fields
            if k == "name" and isinstance(v, str) and any(x in v.lower() for x in ["account", "creds", "api"]):
                new_value = CREDENTIAL_NAME_PLACEHOLDER
            else:
                new_value = sanitize(v)

            if isinstance(v, str):
                # if this key is exactly known sensitive id keys
                if k in SENSITIVE_KEY_EXACT:
                    new_value = SENSITIVE_KEY_EXACT[k]

            # If this is a credentials map typical in n8n
            if k == "credentials" and isinstance(v, dict):
                cred_map = {}
                for cred_type, cred_val in v.items():
                    if isinstance(cred_val, dict):
                        cred_map[cred_type] = {}
                        for ck, cv in cred_val.items():
                            if ck == "id":
                                cred_map[cred_type][ck] = f"{cred_type.upper()}_ID_PLACEHOLDER"
                            elif ck == "name":
                                cred_map[cred_type][ck] = f"Placeholder {cred_type} Credential"
                            else:
                                cred_map[cred_type][ck] = sanitize(cv)
                    else:
                        cred_map[cred_type] = sanitize(cred_val)
                new[k] = cred_map
                continue

            # Some values in known fields
            if new_key == "channelId" and isinstance(v, dict) and v.get("value"):
                new[k] = {**v, "value": "placeholder-channel-name"}
                continue

            if isinstance(v, str) and k in ("id", "webhookId", "formId", "instanceId", "versionId"):
                if k in SENSITIVE_KEY_EXACT:
                    new[k] = SENSITIVE_KEY_EXACT[k]
                    continue

            # fallback
            if isinstance(v, str):
                sanitized = sanitize_value(k, v)
                new[k] = sanitized
            else:
                new[k] = new_value
        return new
    if isinstance(obj, list):
        return [sanitize(item) for item in obj]
    return obj


def main():
    parser = argparse.ArgumentParser(description="Sanitize n8n JSON for public sharing")
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

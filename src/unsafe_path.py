"""STATIC SCAN FIXTURE ONLY — intentionally unsafe; never execute or deploy.

Expected Raksa OpenGrep rule: raksa.python-request-file-access (CWE-22).
This file is not imported by the test suite and must not be run.
"""
from flask import request


def read_user_selected_file() -> str:
    """INSECURE: untrusted request filename is opened without directory confinement."""
    with open(request.args.get("filename"), encoding="utf-8") as handle:
        return handle.read()

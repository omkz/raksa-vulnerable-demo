"""STATIC SCAN FIXTURE ONLY — intentionally unsafe; never execute or deploy.

This file helps verify Raksa's OpenGrep CWE-78 rule. It contains no calls at
module import time and must not be used with real inputs.
"""
import os


def unsafe_command(user_input: str) -> int:
    """INSECURE: command string is passed to a shell without validation."""
    return os.system(user_input)

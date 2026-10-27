"""Intentionally vulnerable teaching example. Never expose this app to a network or run it as a public service."""

import sqlite3


def search_users(connection: sqlite3.Connection, name: str) -> list[tuple[int, str]]:
    query = f"SELECT id, name FROM users WHERE name = '{name}'"
    return connection.execute(query).fetchall()

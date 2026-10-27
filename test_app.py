import sqlite3
import unittest

from app import search_users


class SQLInjectionDemoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.longMessage = False
        self.db = sqlite3.connect(":memory:")
        self.db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        self.db.executemany("INSERT INTO users(name) VALUES (?)", [("alice",), ("bob",), ("charlie",)])

    def tearDown(self) -> None:
        self.db.close()

    def test_normal_search_returns_matching_user(self) -> None:
        rows = search_users(self.db, "alice")
        self.assertEqual(rows, [(1, "alice")])

    def test_sql_injection_payload_is_treated_as_literal(self) -> None:
        rows = search_users(self.db, "' OR 1=1 --")
        self.assertEqual(
            rows,
            [],
            "SQL injection payload returned unexpected rows instead of being treated as a literal search parameter",
        )


if __name__ == "__main__":
    unittest.main()

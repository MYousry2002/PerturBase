#!/usr/bin/env python3

# tests/test_db_connection.py
import unittest
from database.db_utils import get_db_connection

class TestDBConnection(unittest.TestCase):
    def test_connection(self):
        conn = get_db_connection()
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == '__main__':
    unittest.main()
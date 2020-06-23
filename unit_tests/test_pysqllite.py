"""
File: test_pysqllite.py
Date: 4.13.2020
Author: Kyle Lanier

Purpose:
This is a Test Driven Development unittest file intended
on testing functionality as defined within the pysqllite
module.

The pysqllite module is a custom pyhton wrapper for
interactions with a SQLlite databasse. This module is
the core module for this repository.

"""
import os
import sys
import pathlib  # noqa: F401
from pathlib import Path  # for relative path discovery
from unittest import TestCase

# change sys.path
# this allows us to import modules up one directory
file = Path(__file__).resolve()
parent, top = file.parent, file.parents[1]
sys.path.append(os.path.join(top, ''))

from modules.pysqllite import PySQLLite  # noqa: E402


class TestPySQLLite(TestCase):
    """
    TDD unittest file for the PySQLLite module
    """
    def setUp(self):
        """
        To execute before each unittest
        """
        db_location = os.path.join(
            os.path.join(
                os.path.abspath(os.path.join(__file__, '../..')),
                'database'
            ),
            'TEST_WSU_AL.db'
        )
        self.db = PySQLLite(db_location)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS DemoTable (
                id INT PRIMARY KEY,
                description VARCHAR(50)
            );
        """)

    def test_db_execute_exception(self):
        """
        Test the PySQLLite module will raise
        an exception when an invalid statement
        is provided
        """
        with self.assertRaises(Exception) as e:
            self.db.execute("SELECT T")

        exception_message = e.exception.args[0]

        self.assertEqual(
            exception_message,
            'no such column: T'
        )

    def test_db_exit_connection(self):
        """
        Test the PySQLLite module will exit
        a database connection
        """
        # save + close
        self.db.exit()

        with self.assertRaises(Exception) as e:
            self.db.conn.in_transaction

        exception_message = e.exception.args[0]

        self.assertEqual(
            exception_message,
            'Cannot operate on a closed database.'
        )

    def test_db_make_entry(self):
        """
        Test to ensure the PySQLLite module
        will add an entry to a database table
        """
        # Insert data into our demo table
        # This commands is NOT idempotent
        self.db.execute("""
            INSERT OR REPLACE INTO DemoTable VALUES (
                1, "Our first DemoTable record entry"
            );
        """)

        # Fetch the data
        self.db.execute("""
            SELECT * FROM DemoTable
            WHERE id = 1
        """)

        # Pretty print the fetched data
        self.assertEqual(
            self.db.fetchall(),
            [(1, 'Our first DemoTable record entry')]
        )

    def test_db_read_entry(self):
        """
        Test to ensure the PySQLLite module
        can read an entry from a database table
        """
        # Fetch the data
        self.db.execute("""
            SELECT * FROM DemoTable
            WHERE id = 1
        """)

        self.assertEqual(
            self.db.fetchall(),
            [(1, 'Our first DemoTable record entry')]
        )

    def test_db_with_statement(self):
        """
        Test to ensure the PySQLLite module
        will __enter__ and __exit__ when
        used in a with statement
        """
        with self.db:
            # Fetch the data
            self.db.execute("""
                SELECT * FROM DemoTable
                WHERE id = 1
            """)

            self.assertEqual(
                self.db.fetchall(),
                [(1, 'Our first DemoTable record entry')]
            )

    def test_db_delete_entry(self):
        """
        Test to ensure the PySQLLite module
        can delete an entry from a database table
        """
        # Insert data into our demo table
        # This commands is NOT idempotent
        self.db.execute("""
            INSERT INTO DemoTable VALUES (
                2, "Our second DemoTable record entry"
            );
        """)

        # query to check the record
        self.db.execute("""
            SELECT * FROM DemoTable
            WHERE id = 2
        """)

        # ensur the record exists before we delete it
        self.assertEqual(
            self.db.fetchall(),
            [(2, 'Our second DemoTable record entry')]
        )

        # delete the record
        self.db.execute("""
            DELETE FROM DemoTable
            WHERE id = 2
        """)

        # query to check the record
        self.db.execute("""
            SELECT * FROM DemoTable
            WHERE id = 2
        """)

        # ensure the record does not exist
        self.assertEqual(
            self.db.fetchall(),
            []
        )

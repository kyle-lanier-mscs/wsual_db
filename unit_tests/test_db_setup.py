"""
File: db_setup.py
Date: 4.24.2020
Author: Kyle Lanier

Purpose:
This is a Test Driven Development unittest file intended
on testing functionality as defined within the db_setup
module.

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

from modules.db_setup import setup_db  # noqa: E402
from unit_tests.mocks.mock_wsual_db import MOCK_WSUAL_DB  # noqa: E402


class TestDbSetup(TestCase):
    """
    TDD unittest file for the PySQLLite module
    """
    def setUp(self):
        """
        Execute the database setup script and retrieve
        the rendered database
        """
        self.db = setup_db()
        # self.assertEqual(self.db.conn.total_changes, 58)

    def test_db_tables(self):
        """
        Test the WSU_ALDB was successfully created
        """
        self.db.execute(
            "SELECT * FROM sqlite_master"
        )

        wsual_db = self.db.fetchall()

        self.assertEqual(
            wsual_db,
            MOCK_WSUAL_DB
        )

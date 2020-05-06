"""
File: test_suite.py
Date: 4.14.2020
Author: Kyle Lanier

Purpose:
This file is used to import all unittest files to be executed.

This also serves a a singular point of entry for debugging
all unittests. Set your breakpoints within your unittest
file, then come back to this file to execute in debug mode
to step into your breakpoints.

Process:
For every new unittest test file created in the unit_tests
directory, add the respective import statement below. Unittest
main will then execute all unittest modules imported within
this file.

"""
import os
import sys
import pathlib  # noqa: F401
from pathlib import Path  # for relative path discovery
from unittest import main

# change sys.path
# this allows us to import modules up one directory
file = Path(__file__).resolve()
parent, top = file.parent, file.parents[1]
sys.path.append(os.path.join(top, ''))

# now import the unittest files from the higher directory
from unit_tests.test_placeholder_module import TestPlaceholderModule  # noqa: F401
from unit_tests.test_pysqllite import TestPySQLLite  # noqa: F401
from unit_tests.test_db_setup import TestDbSetup  # noqa: F401


main(exit=False)

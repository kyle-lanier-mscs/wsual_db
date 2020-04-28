"""
File: test_placeholder_module.py
Date: 4.17.2020
Author: Kyle Lanier

Porpose:
Its purpose is to serve as a TDD unit test
file to test the placeholder module.

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

from modules.placeholder_module import PlaceholderModule  # noqa: E402


class TestPlaceholderModule(TestCase):
    """
    TDD unit test file to test the placeholder module
    """
    def test_funciton1(self):
        """
        Test (arg1 / arg2) + arg3
        """
        test_module = PlaceholderModule()
        self.assertEqual(
            test_module.function1(6, 2, 2),
            5
        )

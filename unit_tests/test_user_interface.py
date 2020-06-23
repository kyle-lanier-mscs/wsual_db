"""
File: test_user_interface.py
Date: 4.28.2020
Author: Kyle Lanier

Purpose:
This is a Test Driven Development unittest file intended
on testing functionality as defined within the user_interface
module.

"""
import os
import sys
import pathlib  # noqa: F401
from pathlib import Path  # for relative path discovery
from pprint import pprint
from unittest import TestCase
from unittest.mock import patch, call, MagicMock

# change sys.path
# this allows us to import modules up one directory
file = Path(__file__).resolve()
parent, top = file.parent, file.parents[1]
sys.path.append(os.path.join(top, ''))

from modules.pysqllite import PySQLLite  # noqa: E402
from modules.user_interface import get_table, \
    pad_columns, print_table, list_tables, \
    execute_statement, ui_methods, ui_options, \
    ui  # noqa: E402


class TestUserInterface(TestCase):
    """
    TDD unittest file for the user_interface module
    """
    def setUp(self):
        """
        To be executed prior to every test case
        """
        db_location = os.path.join(
            os.path.join(
                os.path.abspath(os.path.join(__file__, '../..')),
                'database'
            ),
            'WSU_AL.db'
        )
        self.db = PySQLLite(db_location)

    @patch('modules.user_interface.input')
    @patch('modules.user_interface.pprint', side_effect=MagicMock(pprint))
    @patch('modules.user_interface.print', side_effect=MagicMock(print))
    def test_execute_statement(self, print, pprint, _input):
        """
        Test the method will execute and return
        a valid statment
        """
        input_return_values = [
            "",
            """
            SELECT studentName from Students
            WHERE studentName='Kyle'
            """
        ]

        _input.side_effect = lambda x: input_return_values.pop()

        execute_statement(self.db)

        pprint.assert_called_with([('Kyle',)])

    def test_list_tables(self):
        """
        Test the method returns a list
        of table names
        """
        table_names = list_tables(self.db)

        self.assertEqual(
            table_names,
            [
                'Skills',
                'SkillSets',
                'Companies',
                'Projects',
                'Purchases',
                'Contracts',
                'Locations',
                'Students',
                'Contains'
            ]
        )

    @patch('modules.user_interface.input')
    @patch('modules.user_interface.print', side_effect=MagicMock(print))
    def test_get_table(self, print, _input):
        """
        Test the WSU_ALDB was successfully returns
        a table
        """
        input_return_values = [
            '1'
        ]

        _input.side_effect = lambda x: input_return_values.pop()

        skillsets_table = get_table(self.db)

        self.assertEqual(
            skillsets_table,
            [
                ('skillSetId INTEGER', 'date TEXT'),
                (1, '2020-04-25'),
                (2, '2020-04-25'),
                (3, '2020-04-25'),
                (4, '2020-04-25'),
                (5, '2020-04-25')
            ]
        )

    @patch('modules.user_interface.input')
    @patch('modules.user_interface.print', side_effect=MagicMock(print))
    def test_pad_columns(self, print, _input):
        """
        Test the WSU_ALDB was successfully returns
        a table that has padded column widths
        """
        input_return_values = [
            '1'
        ]

        _input.side_effect = lambda x: input_return_values.pop()

        skillsets_table = get_table(self.db)

        padded_skillsets_table = pad_columns(skillsets_table)

        self.assertEqual(
            padded_skillsets_table,
            [
                'skillSetId INTEGER  date TEXT           ',
                '1                   2020-04-25          ',
                '2                   2020-04-25          ',
                '3                   2020-04-25          ',
                '4                   2020-04-25          ',
                '5                   2020-04-25          '
            ]
        )

    @patch('modules.user_interface.input')
    @patch('modules.user_interface.print', side_effect=MagicMock(print))
    def test_print_table(self, _print, _input):
        """
        Test the user_interface successfully prints
        a table that has padded column widths
        """
        input_return_values = [
            '1'
        ]

        _input.side_effect = lambda x: input_return_values.pop()

        print_table(self.db)

        _print.assert_any_call('skillSetId INTEGER  date TEXT           ')

    @patch('modules.user_interface.print', side_effect=MagicMock(print))
    def test_ui_options(self, _print):
        """
        Test the user_interface successfully prints
        the intended menu
        """
        ui_options()

        calls = [
            call('[0]: Exit'),
            call('[1]: Execute Statement'),
            call('[2]: Print Table')
        ]

        _print.assert_has_calls(calls)

    def test_ui_exit(self):
        """
        Test the user_interface will successfully exit
        """
        # when the user selects '0' then the
        # assignment method will call sys.exit
        with self.assertRaises(SystemExit):
            ui_methods(self.db, '0')

    @patch('modules.user_interface.input')
    @patch('modules.user_interface.print', side_effect=MagicMock(print))
    def test_ui_exception(self, _print, _input):
        """
        Test the user_interface successfully prints
        an exception message and will exit when
        the user selects option '0'
        """
        input_return_values = [
            '0', "", 'SELECT T', '1'
        ]

        _input.side_effect = lambda x: input_return_values.pop()

        calls = [call('no such column: T')]

        # when the user selects '0' then the
        # assignment method will call sys.exit
        with self.assertRaises(SystemExit):
            ui()

        _print.assert_has_calls(calls)

    # NOTE: After updating the CREATE Table command to
    # cascade on update and delete, this unittest is
    # no longer needed
    #
    # @patch('modules.user_interface.input')
    # @patch('modules.user_interface.print', side_effect=MagicMock(print))
    # def test_foreign_key_constraint(self, _print, _input):
    #     """
    #     Test the method will raise a foreign key
    #     constraint when attempting to delete
    #     a record that is referenced by another
    #     table
    #     """
    #     input_return_values = [
    #         '0',
    #         'DELETE FROM SkillSets WHERE skillSetId = 0',
    #         '1'
    #     ]

    #     _input.side_effect = lambda x: input_return_values.pop()

    #     calls = [call('FOREIGN KEY constraint failed')]

    #     # when the user selects '0' then the
    #     # assignment method will call sys.exit
    #     with self.assertRaises(SystemExit):
    #         ui()

    #     _print.assert_has_calls(calls)

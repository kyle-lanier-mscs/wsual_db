"""
File: user_interface.py
Date: 4.27.2020
Author: Kyle Lanier

Purpose:
This file is used to serve as the main U.I.
for interactions with the pysqlite database

"""
import os
import sys
from pprint import pprint
import pathlib  # noqa: F401
from pathlib import Path  # for relative path discovery

# change sys.path
# this allows us to import modules up one directory
file = Path(__file__).resolve()
parent, top = file.parent, file.parents[1]
sys.path.append(os.path.join(top, ''))

from modules.pysqllite import PySQLLite  # noqa: E402


def ui():
    """
    Capstone user interface method for
    interactions with the pysqlite database
    """
    db_location = os.path.join(
        os.path.join(
            os.path.abspath(os.path.join(__file__, '../..')),
            'database'
        ),
        'WSU_AL.db'
    )

    while True:
        # Connect to a database
        wsual_db = PySQLLite(db_location)
        try:
            print("\n---------WSUAL DB---------")
            ui_options()

            selection = input('\nPlease select an option number:\n> ')

            ui_methods(wsual_db, selection)

        except Exception as e:
            print(e.args[0])


def ui_options():
    """
    Main user interface options list
    """
    options = [
        'Exit',
        'Execute Statement',
        'Print Table'
    ]

    for index, option in enumerate(options):
        print(f"[{index}]: {option}")


def ui_methods(wsual_db, selection=None):
    """
    Main user interface option methods
    """
    methods = {
        '0': lambda: exit(),
        '1': lambda: execute_statement(wsual_db),
        '2': lambda: print_table(wsual_db)
    }

    return [
        lambda: methods,
        lambda: methods[selection]()
    ][int(selection is not None)]()


def execute_statement(wsual_db):
    """
    Prompt user for a SQL statement, then
    execute it
    """
    print("Please enter a blank line to end your statement:")
    statement = ""
    line = " "

    while line != "":
        line = input("> ")
        statement = statement + " " + line

    # Pretty print the fetched data
    pprint(execute(wsual_db, statement))


def execute(wsual_db, statement):
    """
    Method for executing pysqlite statements
    """
    wsual_db.execute(statement)
    results = wsual_db.fetchall()
    return results


def list_tables(wsual_db):
    """
    Simple method for returning a
    list of table names
    """
    return list(
        map(
            lambda x: x[0],
            execute(
                wsual_db,
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
        )
    )


def print_table(wsual_db):
    """
    Method to retreive and print
    the contents of a selected
    table
    """
    table = get_table(wsual_db)

    for row in pad_columns(table):
        print(row)


def pad_columns(table):
    """
    Method to add padded whitespace to
    make table columns print cleanly
    """
    widths = []

    for row in table:
        for col in row:
            widths.append(len(str(col)))

    max_width = max(widths) + 2

    padded_table = []
    for row in table:
        padded_table.append(
            ("".join(str(word).ljust(max_width) for word in row))
        )

    return padded_table


def get_table(wsual_db):
    """
    Metod to prompt user to select a
    table then return the table records
    """
    tables = list_tables(wsual_db)

    print('\nPleasse select a table:')
    for index, table in enumerate(tables):
        print(f"[{index}]: {table}")

    table_name = tables[int(input('> '))]

    schema = get_table_schema(wsual_db, table_name)

    return schema + execute(
        wsual_db,
        f"SELECT * FROM {table_name}"
    )


def get_table_schema(wsual_db, table_name):
    """
    Method to return filtered attributes
    from a table schema
    """
    return [
        tuple(
            map(
                lambda x: f"{x[1]} {x[2]}",
                execute(
                    wsual_db,
                    f"PRAGMA table_info({table_name});"
                )
            )
        )
    ]

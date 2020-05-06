"""
File: db_setup.py
Date: 4.24.2020
Author: Kyle Lanier

Purpose:
This file is used to setup the WSU Applied Learning
database from scratch in the event the database needs
to be recreated.

All methods are designed to be idempotent
"""
import os
import sys
import pathlib  # noqa: F401
from pathlib import Path  # for relative path discovery

# change sys.path
# this allows us to import modules up one directory
file = Path(__file__).resolve()
parent, top = file.parent, file.parents[1]
sys.path.append(os.path.join(top, ''))

from modules.pysqllite import PySQLLite  # noqa: E402
from modules.resources.entities import DEPARTMENTS, \
    COURSES, STUDENTS  # noqa: E402


def setup_db():
    """
    Recreate the database tables, relations, and records
    return the created database for unittest validation
    """
    wsual_db = PySQLLite("database/WSU_AL.db")

    create_tables(wsual_db)
    tables = [
        DEPARTMENTS,
        COURSES,
        STUDENTS
    ]
    enter_tables(wsual_db, tables)

    return wsual_db


def create_tables(wsual_db):
    """
    Create all database tables
    """
    create_departments_table(wsual_db)
    create_courses_table(wsual_db)
    create_students_table(wsual_db)


def enter_tables(wsual_db, tables):
    for table in tables:
        for table_name, records in table.items():
            for record in records:
                enter_record(wsual_db, 'REPLACE', table_name, record)


def enter_record(wsual_db, action, table, values):
    wsual_db.execute(f"INSERT OR {action} INTO {table} VALUES{values}")


def create_departments_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            DId INTEGER NOT NULL,
            DName VARCHAR(30) NOT NULL,
            Abbr VARCHAR(5) NOT NULL,
            PRIMARY KEY(DId),
            CHECK (DId > 0)
        );
    """)


def create_courses_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            CId INTEGER NOT NULL,
            Title VARCHAR(16) NOT NULL,
            DeptId INTEGER NOT NULL,
            PRIMARY KEY(CId),
            FOREIGN KEY(DeptId) REFERENCES Departments,
            CHECK (CId > 0)
        );
    """)


def create_students_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            SId INTEGER NOT NULL,
            SName VARCHAR(12) NOT NULL,
            GradYear INTEGER,
            MajorId INTEGER,
            PRIMARY KEY(SId),
            FOREIGN KEY(MajorId) REFERENCES Departments
                ON DELETE SET NULL
                ON UPDATE CASCADE,
            CHECK (SId > 0),
            CHECK (GradYear >= 1895)
        );
    """)

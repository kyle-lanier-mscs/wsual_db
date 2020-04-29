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
from modules.resources.entities import STUDENTS, SKILLSETS, \
    SKILLS, PROJECTS, CONTRACTS, COMPANIES, LOCATIONS  # noqa: E402
from modules.resources.relations import CONTAINS  # noqa: E402


def setup_db():
    """
    Recreate the database tables, relations, and records
    return the created database for unittest validation
    """
    wsual_db = PySQLLite("database/WSU_AL.db")

    create_tables(wsual_db)
    tables = [
        SKILLS, SKILLSETS,
        COMPANIES, PROJECTS,
        CONTRACTS, LOCATIONS,
        STUDENTS
    ]
    enter_tables(wsual_db, tables)

    create_relations(wsual_db)
    relations = [
        CONTAINS
    ]
    enter_tables(wsual_db, relations)

    return wsual_db


def create_tables(wsual_db):
    """
    Create all database tables
    """
    create_skills_table(wsual_db)
    create_skillsets_table(wsual_db)
    create_companies_table(wsual_db)
    create_projects_table(wsual_db)
    create_contracts_table(wsual_db)
    create_locations_table(wsual_db)
    create_students_table(wsual_db)


def create_students_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            studentId VARCHAR(10) PRIMARY KEY,
            studentName VARCHAR(50) NOT NULL,
            major VARCHAR(50) NOT NULL,
            tenure VARCHAR(20) NOT NULL,
            graduationDate TEXT NOT NULL,
            skillSetId INTEGER NOT NULL,
            locationId VARCHAR(50) NOT NULL,
            FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId),
            FOREIGN KEY(locationId) REFERENCES Locations(locationId)
        );
    """)


def create_skillsets_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS SkillSets (
            skillSetId INTEGER PRIMARY KEY,
            date TEXT NOT NULL
        );
    """)


def create_skills_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Skills (
            skillName VARCHAR(50),
            skillLevel VARCHAR(30) NOT NULL,
            description VARCHAR(50) NOT NULL,
            PRIMARY KEY(skillName, skillLevel)
        );
    """)


def create_projects_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Projects (
            projectId VARCHAR(50) PRIMARY KEY,
            type VARCHAR(50) NOT NULL,
            numStudents INTEGER NOT NULL,
            isRemote BOOL NOT NULL,
            skillSetId INTEGER NOT NULL,
            FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId)
        );
    """)


def create_contracts_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Contracts (
            companyName VARCHAR(50) NOT NULL,
            contractId VARCHAR(50) PRIMARY KEY,
            startDate TEXT NOT NULL,
            endDate TEXT NOT NULL,
            companyManager VARCHAR(50) NOT NULL,
            studentWage REAL NOT NULL,
            cost REAL NOT NULL,
            projectId VARCHAR(50) NOT NULL,
            FOREIGN KEY(companyName) REFERENCES Companies(companyName),
            FOREIGN KEY(projectId) REFERENCES Projects(projectId)
        );
    """)


def create_companies_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Companies (
            companyName VARCHAR(50) PRIMARY KEY,
            abbreviation VARCHAR(20) NOT NULL
        );
    """)


def create_locations_table(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Locations (
            locationId VARCHAR(50) PRIMARY KEY,
            street VARCHAR(50) NOT NULL,
            city VARCHAR(50) NOT NULL,
            state VARCHAR(50) NOT NULL,
            zipcode VARCHAR(10) NOT NULL,
            companyName VARCHAR(50) NOT NULL,
            FOREIGN KEY(companyName) REFERENCES Companies(companyName)
        );
    """)


def enter_tables(wsual_db, tables):
    for table in tables:
        for table_name, records in table.items():
            for record in records:
                enter_record(wsual_db, 'REPLACE', table_name, record)


def enter_record(wsual_db, action, table, values):
    wsual_db.execute(f"INSERT OR {action} INTO {table} VALUES{values}")


def create_relations(wsual_db):
    create_contains_relation(wsual_db)


def create_contains_relation(wsual_db):
    wsual_db.execute("""
        CREATE TABLE IF NOT EXISTS Contains (
            skillSetId INTEGER NOT NULL,
            skillName VARCHAR(50) NOT NULL,
            skillLevel VARCHAR(30) NOT NULL,
            FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId),
            FOREIGN KEY(skillName, skillLevel) REFERENCES Skills(skillName, skillLevel),
            PRIMARY KEY(skillSetId, skillName, skillLevel)
        );
    """)


# def create_matches_relation(wsual_db):
#     wsual_db.execute("""
#         CREATE TABLE IF NOT EXISTS Matches (
#             studentId VARCHAR(10) PRIMARY KEY,
#             skillSetId INTEGER,
#             FOREIGN KEY(studentId) REFERENCES Students(studentId),
#             FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId)
#         );
#     """)


# def create_requires_relation(wsual_db):
#     wsual_db.execute("""
#         CREATE TABLE IF NOT EXISTS Requires (
#             skillSetId INTEGER,
#             projectId VARCHAR(50),
#             FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId),
#             FOREIGN KEY(projectId) REFERENCES Projects(projectId)
#         );
#     """)


# def create_defines_relation(wsual_db):
#     wsual_db.execute("""
#         CREATE TABLE IF NOT EXISTS Defines (
#             projectId VARCHAR(50),
#             contractId VARCHAR(50),
#             FOREIGN KEY(projectId) REFERENCES Projects(projectId),
#             FOREIGN KEY(contractId) REFERENCES Contracts(contractId)
#         );
#     """)


# def create_grants_relation(wsual_db):
#     wsual_db.execute("""
#         CREATE TABLE IF NOT EXISTS Grants (
#             companyName VARCHAR(50) NOT NULL,
#             contractId VARCHAR(50) NOT NULL,
#             FOREIGN KEY(companyName) REFERENCES Companies(companyName),
#             FOREIGN KEY(contractId) REFERENCES Contracts(contractId),
#             PRIMARY KEY(companyName, contractId)
#         );
#     """)


# def create_located_relation(wsual_db):
#     wsual_db.execute("""
#         CREATE TABLE IF NOT EXISTS Located (
#             companyName VARCHAR(50),
#             locationId VARCHAR(50),
#             FOREIGN KEY(companyName) REFERENCES Companies(companyName),
#             FOREIGN KEY(locationId) REFERENCES Locations(locationId)
#         );
#     """)


# def create_near_relation(wsual_db):
#     wsual_db.execute("""
#         CREATE TABLE IF NOT EXISTS Near (
#             studentId VARCHAR(10) NOT NULL,
#             locationId VARCHAR(50) NOT NULL,
#             FOREIGN KEY(studentId) REFERENCES Students(studentId),
#             FOREIGN KEY(locationId) REFERENCES Locations(locationId),
#             PRIMARY KEY(studentId, locationId)
#         );
#     """)

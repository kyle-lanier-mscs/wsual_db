"""
File: /modules/db_setup.py
Date: 4.24.2020
Author: Kyle Lanier

Purpose:
This file is used to setup the WSU Applied Learning
database from scratch in the event the database needs
to be recreated. All methods are designed to be idempotent.


def setup_db():
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates entire database
        :param None:
        :type None:
        :return: the rendered wsual_db
        :rtype: sqlite3 database


def create_tables(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates all tables
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None


def create_students_table(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates Students table
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None

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


def create_skillsets_table(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates SkillSets table
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None

        CREATE TABLE IF NOT EXISTS SkillSets (
            skillSetId INTEGER PRIMARY KEY,
            date TEXT NOT NULL
        );


def create_skills_table(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates Skills table
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None

        CREATE TABLE IF NOT EXISTS Skills (
            skillName VARCHAR(50),
            skillLevel VARCHAR(30) NOT NULL,
            description VARCHAR(50) NOT NULL,
            PRIMARY KEY(skillName, skillLevel)
        );


def create_projects_table(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates Projects table
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None

        CREATE TABLE IF NOT EXISTS Projects (
            projectId VARCHAR(50) PRIMARY KEY,
            type VARCHAR(50) NOT NULL,
            numStudents INTEGER NOT NULL,
            isRemote BOOL NOT NULL,
            skillSetId INTEGER NOT NULL,
            FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId)
        );


def create_contracts_table(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates Contracts table
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None

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


def create_companies_table(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates Companies table
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None

        CREATE TABLE IF NOT EXISTS Companies (
            companyName VARCHAR(50) PRIMARY KEY,
            abbreviation VARCHAR(20) NOT NULL
        );


def create_locations_table(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates Locations table
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None

        CREATE TABLE IF NOT EXISTS Locations (
            locationId VARCHAR(50) PRIMARY KEY,
            street VARCHAR(50) NOT NULL,
            city VARCHAR(50) NOT NULL,
            state VARCHAR(50) NOT NULL,
            zipcode VARCHAR(10) NOT NULL,
            companyName VARCHAR(50) NOT NULL,
            FOREIGN KEY(companyName) REFERENCES Companies(companyName)
        );


def enter_tables(wsual_db, tables):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: batch create or update one or more tables
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :param tables: list of sqlite3 tables to be updated
        :type list:
        :return: None
        :rtype: None

        for table in tables:
            for table_name, records in table.items():
                for record in records:
                    enter_record(wsual_db, 'REPLACE', table_name, record)


def enter_record(wsual_db, action, table, values):
    wsual_db.execute(f"INSERT OR {action} INTO {table} VALUES{values}")


def create_relations(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates all relational tables
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None


def create_contains_relation(wsual_db):
    - **purpose**, **parameters**, **types**, **return** and **return types**::

        :purpose: creates Contains table
        :param wsual_db: the WSU applied learning database
        :type sqlite3: sqlite3 database
        :return: None
        :rtype: None

        CREATE TABLE IF NOT EXISTS Contains (
            skillSetId INTEGER NOT NULL,
            skillName VARCHAR(50) NOT NULL,
            FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId),
            FOREIGN KEY(skillName, skillLevel) REFERENCES Skills(skillName, skillLevel),
            PRIMARY KEY(skillSetId, skillName, skillLevel)
        );

"""

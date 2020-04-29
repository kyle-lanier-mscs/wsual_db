MOCK_WSUAL_DB = [
    (
        'table',
        'Skills',
        'Skills',
        2,
        'CREATE TABLE Skills (\n'
        '            skillName VARCHAR(50),\n'
        '            skillLevel VARCHAR(30) NOT NULL,\n'
        '            description VARCHAR(50) NOT NULL,\n'
        '            PRIMARY KEY(skillName, skillLevel)\n'
        '        )'),
    ('index', 'sqlite_autoindex_Skills_1', 'Skills', 3, None),
    (
        'table',
        'SkillSets',
        'SkillSets',
        4,
        'CREATE TABLE SkillSets (\n'
        '            skillSetId INTEGER PRIMARY KEY,\n'
        '            date TEXT NOT NULL\n'
        '        )'),
    (
        'table',
        'Companies',
        'Companies',
        5,
        'CREATE TABLE Companies (\n'
        '            companyName VARCHAR(50) PRIMARY KEY,\n'
        '            abbreviation VARCHAR(20) NOT NULL\n'
        '        )'),
    ('index', 'sqlite_autoindex_Companies_1', 'Companies', 6, None),
    (
        'table',
        'Projects',
        'Projects',
        7,
        'CREATE TABLE Projects (\n'
        '            projectId VARCHAR(50) PRIMARY KEY,\n'
        '            type VARCHAR(50) NOT NULL,\n'
        '            numStudents INTEGER NOT NULL,\n'
        '            isRemote BOOL NOT NULL,\n'
        '            skillSetId INTEGER NOT NULL,\n'
        '            FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId)\n'
        '        )'),
    ('index', 'sqlite_autoindex_Projects_1', 'Projects', 8, None),
    (
        'table',
        'Contracts',
        'Contracts',
        9,
        'CREATE TABLE Contracts (\n'
        '            companyName VARCHAR(50) NOT NULL,\n'
        '            contractId VARCHAR(50) PRIMARY KEY,\n'
        '            startDate TEXT NOT NULL,\n'
        '            endDate TEXT NOT NULL,\n'
        '            companyManager VARCHAR(50) NOT NULL,\n'
        '            studentWage REAL NOT NULL,\n'
        '            cost REAL NOT NULL,\n'
        '            projectId VARCHAR(50) NOT NULL,\n'
        '            FOREIGN KEY(companyName) REFERENCES Companies(companyName),\n'
        '            FOREIGN KEY(projectId) REFERENCES Projects(projectId)\n'
        '        )'),
    ('index', 'sqlite_autoindex_Contracts_1', 'Contracts', 10, None),
    (
        'table',
        'Locations',
        'Locations',
        11,
        'CREATE TABLE Locations (\n'
        '            locationId VARCHAR(50) PRIMARY KEY,\n'
        '            street VARCHAR(50) NOT NULL,\n'
        '            city VARCHAR(50) NOT NULL,\n'
        '            state VARCHAR(50) NOT NULL,\n'
        '            zipcode VARCHAR(10) NOT NULL,\n'
        '            companyName VARCHAR(50) NOT NULL,\n'
        '            FOREIGN KEY(companyName) REFERENCES Companies(companyName)\n'
        '        )'),
    ('index', 'sqlite_autoindex_Locations_1', 'Locations', 12, None),
    (
        'table',
        'Students',
        'Students',
        13,
        'CREATE TABLE Students (\n'
        '            studentId VARCHAR(10) PRIMARY KEY,\n'
        '            studentName VARCHAR(50) NOT NULL,\n'
        '            major VARCHAR(50) NOT NULL,\n'
        '            tenure VARCHAR(20) NOT NULL,\n'
        '            graduationDate TEXT NOT NULL,\n'
        '            skillSetId INTEGER NOT NULL,\n'
        '            locationId VARCHAR(50) NOT NULL,\n'
        '            FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId),\n'
        '            FOREIGN KEY(locationId) REFERENCES Locations(locationId)\n'
        '        )'),
    ('index', 'sqlite_autoindex_Students_1', 'Students', 14, None),
    (
        'table',
        'Contains',
        'Contains',
        15,
        'CREATE TABLE Contains (\n'
        '            skillSetId INTEGER NOT NULL,\n'
        '            skillName VARCHAR(50) NOT NULL,\n'
        '            skillLevel VARCHAR(30) NOT NULL,\n'
        '            FOREIGN KEY(skillSetId) REFERENCES SkillSets(skillSetId),\n'
        '            FOREIGN KEY(skillName, skillLevel) REFERENCES Skills(skillName, '
        'skillLevel),\n'
        '            PRIMARY KEY(skillSetId, skillName, skillLevel)\n'
        '        )'),
    ('index', 'sqlite_autoindex_Contains_1', 'Contains', 16, None)
]

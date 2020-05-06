MOCK_WSUAL_DB = [
    (
        'table',
        'Departments',
        'Departments',
        2,
        'CREATE TABLE Departments (\n'
        '            DId INTEGER NOT NULL,\n'
        '            DName VARCHAR(30) NOT NULL,\n'
        '            Abbr VARCHAR(5) NOT NULL,\n'
        '            PRIMARY KEY(DId),\n'
        '            CHECK (DId > 0)\n'
        '        )'),
    (
        'table',
        'Courses',
        'Courses',
        3,
        'CREATE TABLE Courses (\n'
        '            CId INTEGER NOT NULL,\n'
        '            Title VARCHAR(16) NOT NULL,\n'
        '            DeptId INTEGER NOT NULL,\n'
        '            PRIMARY KEY(CId),\n'
        '            FOREIGN KEY(DeptId) REFERENCES Departments,\n'
        '            CHECK (CId > 0)\n'
        '        )'),
    (
        'table',
        'Students',
        'Students',
        4,
        'CREATE TABLE Students (\n'
        '            SId INTEGER NOT NULL,\n'
        '            SName VARCHAR(12) NOT NULL,\n'
        '            GradYear INTEGER,\n'
        '            MajorId INTEGER,\n'
        '            PRIMARY KEY(SId),\n'
        '            FOREIGN KEY(MajorId) REFERENCES Departments\n'
        '                ON DELETE SET NULL\n'
        '                ON UPDATE CASCADE,\n'
        '            CHECK (SId > 0),\n'
        '            CHECK (GradYear >= 1895)\n'
        '        )'
    )
]

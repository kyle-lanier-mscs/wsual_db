"""
File: main.py
Author: Kyle Lanier

Purpose:
This file is used to call the main U.I.
for interactions with the pysqlite database

:Example:

>>> main()
>>> ---------WSUAL DB---------
>>> [0]: Exit
>>> [1]: Execute Statement
>>> [2]: Print Table
>>> 1
>>>
>>> Please enter a blank line to end your statement:
>>> SELECT *
>>> FROM Students
>>> WHERE SName='Joe'
>
[(1, 'Joe', 2020, 10)]
>>>
>>> ---------WSUAL DB---------
>>> [0]: Exit
>>> [1]: Execute Statement
>>> [2]: Print Table
>>> 2
>>>
>>> Pleasse select a table:
>>> [0]: Departments
>>> [1]: Courses
>>> [2]: Students
>>> 0
DId INTEGER        DName VARCHAR(30)  Abbr VARCHAR(5)
10                 Computer Science   CS
20                 Mathematics        Math
30                 English            Engl

"""

from modules.user_interface import ui


if __name__ == '__main__':
    ui()

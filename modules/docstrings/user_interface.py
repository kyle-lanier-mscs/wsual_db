"""
File: /modules/user_interface.py
Date: 4.27.2020
Author: Kyle Lanier

Purpose:
This file is used to serve as the main U.I.
for interactions with the pysqlite database


def ui():
    :Example:

    >>> ui()
    >>> ---------WSUAL DB---------
    >>> [0]: Exit
    >>> [1]: Execute Statement
    >>> [2]: Print Table
    >>> 1
    >>> Please enter a statement: SELECT * FROM Students WHERE studentName='Kyle'
    >>> [('y839k364', 'Kyle', 'CS', 'Graduate', '2021-05-25', 1, 'WSU Wichita')]
    >>>
    >>>
    >>> ---------WSUAL DB---------
    >>> [0]: Exit
    >>> [1]: Execute Statement
    >>> [2]: Print Table
    >>> 2
    >>>
    >>> Pleasse select a table:
    >>> [0]: Students
    >>> [1]: SkillSets
    >>> [2]: Skills
    >>> [3]: Projects
    >>> [4]: Contracts
    >>> [5]: Companies
    >>> [6]: Locations
    >>> [7]: Contains
    >>> 2
    skillName VARCHAR(50)    skillLevel VARCHAR(30)   description VARCHAR(50)
    Python                   High                     CS Programming
    Power BI                 Medium                   Data Analytics
    AWS                      Low                      Cloud Services
    Office 365               Medium                   Microsoft Applications
    Technical Support        Medium                   Support Services
    Azure                    Low                      Cloud Services
    C#                       Low                      CS Programming
    Customer Service         High                     Support Services
    MySQL                    Low                      Data Analytics

"""

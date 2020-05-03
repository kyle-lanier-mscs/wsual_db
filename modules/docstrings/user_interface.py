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
    >>>
    >>> Please enter a blank line to end your statement:
    >>> SELECT S.studentName, T.date
    >>> FROM Students as S
    >>> JOIN Skillsets as T
    >>> ON S.skillSetId=T.skillSetId
    >>> WHERE S.studentName='Kyle'
    >>>
    [('Kyle', '2020-04-25')]
    >>>
    >>>
    >>> ---------WSUAL DB---------
    >>> [0]: Exit
    >>> [1]: Execute Statement
    >>> [2]: Print Table
    >>> 2
    >>>
    >>> Pleasse select a table:
    >>> [0]: Skills
    >>> [1]: SkillSets
    >>> [2]: Companies
    >>> [3]: Projects
    >>> [4]: Purchases
    >>> [5]: Contracts
    >>> [6]: Locations
    >>> [7]: Students
    >>> [8]: Contains
    >>> 0
    >>>
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

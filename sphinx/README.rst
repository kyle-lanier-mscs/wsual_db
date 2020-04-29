WSU\_ALDB
=========

-  Wichita State University Applied Learning database
-  Front-end user interfaces: `QA <https://wsualdb-qa.kyle-lanier.repl.run>`__,
   `Dev <https://wsualdb-dev.kyle-lanier.repl.run>`__,
   `Prod <https://wsualdb-prod.kyle-lanier.repl.run>`__
-  Source code can be accessed at: `Github <https://github.com/kyle-lanier-mscs/wsual_db/>`__
-  This repository is developed by TDD serverless CICD build processes
-  Flake8 linting, unittests, and coverage are enforced for build
   quality
-  Compatible with Python 3.6.x, Windows, Linux, Mac

CONTENTS
--------

-  `Documentation <#documentation>`__
-  `Goals <#goals>`__
-  `Installation <#Installation>`__
-  `CICD <#cicd>`__
-  `Contribute <#contribute>`__
-  `Troubleshooting <#troubleshooting>`__

Documentation
-------------
.. figure:: ../resources/Detailed_Description.png
   :alt: 

.. figure:: ../resources/ER_Diagram.png
   :alt: 

.. figure:: ../resources/Relational_Schemas.png
   :alt: 

Goals
-----
   * What skills are in demand by local businesses?
   * Who are the closest hire-ready students for a project?
   * What positions do we need to prepare for backfill?

Installation
------------
   First install python and pip because this program will automatically execute pip commands
   to install packages based on how you use this repository. After you download or cloan this 
   repository, use your commandline to change directory into the root folder and execute main.py

   * Python3
   * pip

CICD
----
   This repository follows test driven development practices. In order to self-validate unittests,
   and flake8 linting, in the root folder you can exectue (>python ./cicd/cicd_validation.py). 

   Flake8 linting, unittest validation, and code coverage will then be analyzed. Expect github
   to deny push/pull requests on protected branches if cicd_validation.py is not satisfied.

   To automatically update the sphinx documentation and upload the wiki to a hosting service,
   from within the root folder you can execute (>python ./cicd/sphinx_docgen.py).

   Note: to execute sphinx_docgen.py you will need to set your .env in the root directory and
   establish your own hosting service for the sphinx wiki.

CONTRIBUTE
----------
   This repository follows test driven development practices and the steps below define
   the process to contribute future enhancements.

   1: Clone the dev branch and change directory into the root folder

   2: From the commandline create a new branch, examples include:
      git checkout -b feat/my_feature

   3: Create or update the necessary files within:
      /modules
      /unit_tests

   4: Import your new unittest file within the following script
      /cicd/test_suite.py

   5: Create or update the appropriate docstring file located in
      /modules/docstrings

   6: Pre validate your code by executing the validation script
      /cicd/cicd_valaidation.py

   7: Regenerate the sphinx wiki by executing the following script
      /cicd/sphinx_docgen.py

Troubleshooting
---------------
   All unittest files located in the unit_tests directory can be debugged using /cicd/test_suite.py

   Set your breakpoints anywhere in a unittest file located withn the unit_tests directory.
   Then execute the /cicd/test_suite.py file using debug mode (Visual Studio Code) to step
   into your breakpoints. For each unittest file that is added into the /unit_tests
   directory, be sure to add the respective import within /cicd/test_suite.py

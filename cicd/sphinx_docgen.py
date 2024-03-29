"""
File: sphinx_docgen.py
Date: 4.15.2020
Author: Kyle Lanier

Purpose:
This file is used to automatically generate documentation
for the repository by using sphinx to analyze doc strings
within python files.

Process:
First we import the necessary modules. Then we use sphinx
to analyze the repro and create the wiki in the sphinx
_build directory. Finally, we then execute a sync to
host the wiki.

This file can be executed locally from the root directory
prior to the submission of pull or merge requests.

Note: You will need to set your own .env variable
to your own hosting service

"""
import os


if __name__ == '__main__':
    print('\nExecuting Sphinx Document Generation\n')
    os.system('pip install sphinx')
    os.system('pip install python-dotenv')

    print(f"{os.path.join('sphinx', '_build')}")

    sphinx = os.path.join(
        os.path.abspath(os.path.join(__file__, '../..')),
        'sphinx'
    )

    sphinx_build = os.path.join(
        sphinx,
        '_build'
    )

    os.system(f"sphinx-apidoc -o {sphinx} .")

    os.system(f"sphinx-build -b html {sphinx} {sphinx_build}")

    print('\nExecuting Hosting Serivice Sync\n')
    # from dotenv import load_dotenv
    # load_dotenv()
    # SPHINX_SYNC = os.getenv('SPHINX_SYNC')
    # os.system(f"{SPHINX_SYNC}")

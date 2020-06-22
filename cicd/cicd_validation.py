"""
File: cicd_validation.py
Date: 4.15.2020
Author: Kyle Lanier

Porpose:
Its purpose is to serve the developer as a single point of
entry to execute and validate flake8, unittests, and code
coverage.

Expect github to deny builds for protected branches if
this file is not satisfied.

This file can be executed locally from the root directory
prior to the submission of pull or merge requests.

"""
import os


if __name__ == '__main__':
    print('\nExecuting Flake8 Linting Validation\n')
    f8 = 'analyze_flake8.py'
    os.system(
        "python "
        f"{os.path.join(os.path.dirname(os.path.realpath(__file__)), f8)}"
    )

    print('\nExecuting Unittests and Coverage\n')
    ac = 'analyze_coverage.py'
    os.system(
        "python "
        f"{os.path.join(os.path.dirname(os.path.realpath(__file__)), ac)}"
    )

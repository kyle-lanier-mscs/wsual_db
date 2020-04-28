"""
File: analyze_flake8.py
Date: 4.14.2020
Author: Kyle Lanier

Porpose:
This file is an abstraction from the .github workflows cicd.yml
and its purpose is to analyze flake8 linting errors locally in
the repository. The cicd.yml is used in the github docker runtime
and cannot be executed locally, hence this python file enables
the developer to validate flake8 enforcement locally.

Note: We still need the commands to be included within the
cicd.yml else the gitgub docker container will not stop
the build on failed linting detection.

The github workflow will fail push/pull requests if flake8
linting standards are not satisfied.

This file can be executed locally from the root directory
prior to the submission of pull or merge requests.

Process:
First we import the necessary modules. Then we use the flake8
module to execute and analyze all files within the repository
for flake8 linting errors.

"""
import os


if __name__ == '__main__':
    os.system('pip install flake8')
    print('\nExecuting Flake8 Linting Analysis\n')

    # Check for Python syntax errors or undefined names
    os.system('flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics')
    os.system('flake8 . --count --max-complexity=10 --max-line-length=127 --statistics')

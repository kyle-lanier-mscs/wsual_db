"""
File: analyze_coverage.py
Date: 4.15.2020
Author: Kyle Lanier

Purpose:
This file is an abstraction from the .github workflows cicd.yml
where within the cicd.yml we use Pytest to validate unit testing
within the build workflow. We use Pytest in the cicd.yml instead
of the native unittest module because the unittest module will
not stop the build if a unittest fails.

However, the native unittest module is very good at generating
clean coverage reports. So, we use Pytest in the cicd.yml to
enforce unittests in the github build process, and we use
the coverage and unittest modules here to generate meaningful
reports.

This file can be executed locally from the root directory
prior to the submission of pull or merge requests.

Process:e
First we import the necessary modules. Then we use the coverage
module to execute and analyze all unittests. A .coverage report
is then generated and converted into a bage for use within the
README which displays on github. After the badge is generated the
last thing we do is remove the stale .coverage report.

"""
import os


if __name__ == '__main__':
    os.system('pip install coverage')
    os.system('pip install coverage-badge')

    print('\nExecuting Test Driven Development UnitTests\n')
    os.system(f"coverage run ./cicd/test_suite.py")

    print('\nExecuting Coverage Report\n')
    os.system('coverage report -m --omit=*\\__init__.py')

    print('\nGenerating Coverage Badge\n')
    os.system(f"coverage-badge -o {os.path.join('resources', 'coverage.svg')} -f")
    os.system('coverage erase')

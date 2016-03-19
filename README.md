# Python Library Cookie Cutter

Project template for a simple, open source, python library.

Includes:

 -  Basic project structure, including a `README.md`, an open source (Apache 2) `LICENSE`,
    a sane `.gitignore`, and `setuptools` configuration.

 -  CI configuration via [tox](https://testrun.org/tox/latest/), [CircleCI](https://circleci.com),
    [PullApprove](https://pullapprove.com/), and [BumpVersion](https://pypi.python.org/pypi/bumpversion)

 -  Stub testing support with [nose](http://nose.readthedocs.org/en/latest/writing_tests.html),
    [PyHamcrest](https://github.com/hamcrest/PyHamcrest), [flake8](http://flake8.readthedocs.org/en/latest/index.html),
    and [coverage](http://coverage.readthedocs.org/en/latest/)


## Usage

 1. Install [cookiecutter](https://github.com/audreyr/cookiecutter):

        pip install cookiecutter

 2. Change to an appropriate working directory.

 3. Run cookiecutter against this repository:

        cookiecutter https://github.com/globality-corp/cookiecutter-python-library

 4. Answer the questions. Be sure to provide an appropriate value for the `project_name`,
    `repo_name`, and `short_description`.

 5. Change into the `{{ repo_name }}` directory and initialize a new git project from there.

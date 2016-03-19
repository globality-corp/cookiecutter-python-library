#!/usr/bin/env python
from setuptools import find_packages, setup

project = "{{cookiecutter.project_name}}"
version = "{{cookiecutter.version_version}}"

setup(
    name=project,
    version=version,
    description="{{cookiecutter.short_description}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    url="https://github.com/{{cookiecutter.organization_name}}/{{cookiecutter.repo_name}}",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    setup_requires=[
        "nose>=1.3.6",
    ],
    dependency_links=[
    ],
    entry_points={
    },
    tests_require=[
        "coverage>=3.7.1",
        "mock>=1.0.1",
        "PyHamcrest>=1.8.5",
    ],
)

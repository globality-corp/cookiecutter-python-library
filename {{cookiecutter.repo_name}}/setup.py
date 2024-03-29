#!/usr/bin/env python
from setuptools import find_packages, setup

project = "{{cookiecutter.project_name}}"
version = "{{cookiecutter.project_version}}"

setup(
    name=project,
    version=version,
    description="{{cookiecutter.short_description}}",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.author_email}}",
    url="https://github.com/{{cookiecutter.organization_name}}/{{cookiecutter.repo_name}}",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    dependency_links=[
    ],
    entry_points={
    },
    extras_require = {
        "test": [
            "coverage>=3.7.1",
            "mock>=1.0.1",
        ],
    },
)

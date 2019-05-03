#!/usr/bin/env python

from setuptools import setup

PROJECT = "beehive"

setup(
    name=PROJECT,
    version="0.1",
    author="Stéphane Raimbault",
    author_email="stephane.raimbault@gmail.com",
    license="BSD 3-clause",
    packages=[PROJECT],
    include_package_data=True,
    install_requires=[
        "Flask~=1.0.2",
        "Flask-SQLAlchemy~=2.3.2",
        "psycopg2-binary~=2.8.2",
        "SQLAlchemy~=1.3.0",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=["Programming Language :: Python :: 3"],
)

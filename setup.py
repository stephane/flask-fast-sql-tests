#!/usr/bin/env python

import pip
from pip.req import parse_requirements
from setuptools import setup

PROJECT = 'beehive'

requirements = parse_requirements('requirements.txt', session=pip.download.PipSession())
install_requires = [str(r.req) for r in requirements]

setup(
    name=PROJECT,
    version="0.1",
    author="Stéphane Raimbault",
    author_email="stephane.raimbault@gmail.com",
    license="BSD 3-clause",
    packages=[PROJECT],
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

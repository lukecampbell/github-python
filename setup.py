#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [req for req in open('requirements.txt')]


def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name="github-python",
    version='0.0.1',
    description='Simple python command-line tool to simplify interfacing with github',
    long_description=readme(),
    author='Luke Campbell',
    author_email='luke.s.campbell@gmail.com',
    py_modules=['github'],
    entry_points={
        'console_scripts': [
            'github = github:main'
        ]
    }
)


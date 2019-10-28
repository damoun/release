#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    author="Damien PLENARD",
    author_email='damien@plenard.me',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Retrieve games release dates and create an ical.",
    license="MIT License",
    long_description=README,
    name='release',
    packages=('release'),
    project_urls={
        'Maintainer': 'https://github.com/damoun',
        'Source': 'https://github.com/damoun/release',
        'Tracker': 'https://github.com/damoun/release/issues'
    },
    version="0.0.1"
)

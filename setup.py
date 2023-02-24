#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Setup dot py."""
from __future__ import absolute_import, print_function

# import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read description files."""
    path = join(dirname(__file__), *names)
    with open(path, encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


setup(
    name='speakclouder-monitoringy',
    version='0.0.1',
    description='Python package for creating AWS Cloudwatch dashboards using a config.yaml file',
    license='MIT License',
    author='Stu Mason',
    author_email='stu@speakcloud.consulting',
    url='https://github.com/speakclouder/monitoringy',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    project_urls={
        'webpage': 'https://github.com/speakclouder/monitoringy',
        'Documentation': 'https://monitoringy.readthedocs.io/en/latest/',
        'Changelog': 'https://github.com/speakclouder/monitoringy/blob/main/CHANGELOG.md',
        'Issue Tracker': 'https://github.com/speakclouder/monitoringy/issues',
        'Discussion Forum': 'https://github.com/speakclouder/monitoringy/discussions',
        },
    keywords=[
        'aws', 'monitoring', 'cloudwatch', 'dashboard'
        ],
    python_requires='>=3.8, <4',
    )

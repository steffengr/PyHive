#!/usr/bin/env python

from setuptools import setup
from setuptools.command.test import test as TestCommand
import pyhive
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name="PyHopsHive",
    version=pyhive.__version__,
    description="Python interface to Hops Hive",
    long_description=long_description,
    url='https://github.com/logicalclocks/PyHive',
    author="Jing Wang, Fabio Buso",
    author_email="jing@dropbox.com, fabio@logicalclocks.com",
    license="Apache License, Version 2.0",
    packages=['pyhive', 'TCLIService'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Database :: Front-Ends",
    ],
    install_requires=[
        'future',
        'pyjks',
        'python-dateutil',
    ],
    extras_require={
        'presto': ['requests>=1.0.0'],
        'hive': ['sasl>=0.2.1', 'thrift>=0.10.0', 'thrift_sasl>=0.1.0'],
        'sqlalchemy': ['sqlalchemy>=0.8.7'],
    },
    tests_require=[
        'mock>=1.0.0',
        'pytest',
        'pytest-cov',
        'requests>=1.0.0',
        'sasl>=0.2.1',
        'sqlalchemy>=0.12.0',
        'thrift>=0.10.0',
    ],
    cmdclass={'test': PyTest},
    package_data={
        '': ['*.rst'],
    },
    entry_points={
        'sqlalchemy.dialects': [
            'hive = pyhive.sqlalchemy_hive:HiveDialect',
            'presto = pyhive.sqlalchemy_presto:PrestoDialect',
        ],
    }
)

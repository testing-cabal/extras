#!/usr/bin/env python
"""Distutils installer for extras."""

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand
import os.path

import extras

class TestTools(TestCommand):
    buffer = 0
    catch = 0

    def run_tests(self):
        # import testtools here in case testtools is not installed.
        # testtools is guaranteed to be installed now since tests_require
        # will install it if need be.
        import testtools

        argv = [self.test_suite]

        if self.buffer:
            argv.append('--buffer')

        if self.catch:
            argv.append('--catch')

        errno = testtools.run.main(argv, sys.stdout)
        sys.exit(errno)

def get_version():
    """Return the version of extras that we are building."""
    version = '.'.join(
        str(component) for component in extras.__version__[0:3])
    return version


def get_long_description():
    readme_path = os.path.join(
        os.path.dirname(__file__), 'README.rst')
    return open(readme_path).read()


setup(name='extras',
      author='Testing cabal',
      author_email='testtools-dev@lists.launchpad.net',
      url='https://github.com/testing-cabal/extras',
      description=('Useful extra bits for Python - things that shold be '
        'in the standard library'),
      long_description=get_long_description(),
      version=get_version(),
      classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        ],
      packages=[
        'extras',
        'extras.tests',
        ],
      tests_require=['testtools'],
      cmdclass={'test': TestTools})

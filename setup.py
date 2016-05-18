#!/usr/bin/env python
"""Distutils installer for extras."""

from setuptools import setup
import os.path

import extras
testtools_cmd = extras.try_import('testtools.TestCommand')


def get_version():
    """Return the version of extras that we are building."""
    version = extras.__version__
    return version


def get_long_description():
    readme_path = os.path.join(
        os.path.dirname(__file__), 'README.rst')
    return open(readme_path).read()


cmdclass = {}

if testtools_cmd is not None:
    cmdclass['test'] = testtools_cmd


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
      cmdclass=cmdclass)

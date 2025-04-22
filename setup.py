#!/usr/bin/env python3
"""Distutils installer for extras."""

from setuptools import setup, Command
import os.path
from typing import cast

import extras

testtools_cmd = cast(Command, extras.try_import("testtools.TestCommand"))


def get_version() -> str:
    """Return the version of extras that we are building."""
    version = ".".join(str(component) for component in extras.__version__[0:3])
    return version


def get_long_description() -> str:
    readme_path = os.path.join(os.path.dirname(__file__), "README.rst")
    with open(readme_path) as f:
        return f.read()


cmdclass: dict[str, type[Command]] = {}

if testtools_cmd is not None:
    cmdclass["test"] = testtools_cmd


setup(
    name="extras",
    author="Testing cabal",
    author_email="testtools-dev@lists.launchpad.net",
    url="https://github.com/testing-cabal/extras",
    description=(
        "Useful extra bits for Python - things that should be in the standard library"
    ),
    long_description=get_long_description(),
    version=get_version(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=[
        "extras",
        "extras.tests",
    ],
    package_data={"extras": ["py.typed"]},
    cmdclass=cmdclass,
)

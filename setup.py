#!/usr/bin/env python3

from __future__ import annotations

from sys import argv

from setuptools import setup

__version__ = "0.0.0"

try:
    from semantic_release import setup_hook

    setup_hook(argv)
except ImportError:
    pass

setup(
    name="get-comics",
    version=__version__,
)

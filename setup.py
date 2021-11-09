#!/usr/bin/env python
import os
from setuptools import setup

setup(
    name="files_analyser",
    version="1.0dev",
    py_modules=["files_analyser"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "files_analyser = files_analyser:hello",
        ],
    },
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
    url="https://github.com/TrywialnyOrzech/KRYCY",
    author="Natan Orzechowski, Warsaw University of Technology",
    author_email="natan.orzechowski@comcert.pl",
)
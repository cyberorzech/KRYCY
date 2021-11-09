#!/usr/bin/env python
import os
from setuptools import find_packages, setup

setup(
    name="files_analyser",
    version="1.0dev",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "files_analyser = files_analyser:hello",
            "test_script = test_script:how_ru",
        ],
    },
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
    url="https://github.com/TrywialnyOrzech/KRYCY",
    author="Natan Orzechowski, ComCERT S.A.",
    author_email="natan.orzechowski@comcert.pl",
)
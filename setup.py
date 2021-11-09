#!/usr/bin/env python
import os
from setuptools import setup

setup(
    name="lab1",
    version="1.0dev",
    packages=["src/", "tests/"],
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
    url="https://github.com/TrywialnyOrzech/KRYCY",
    author="Natan Orzechowski, Warsaw University of Technology",
    author_email="natan.orzechowski@comcert.pl",
)
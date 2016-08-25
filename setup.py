#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
    setuptools_available = True
except ImportError:
    from distutils.core import setup
    setuptools_available = False


params = {}
if setuptools_available:
    params['entry_points'] = {'console_scripts': ['jwis = jwis:main']}
else:
    params['scripts'] = ['bin/jwis']


setup(
    name="jwis",
    packages=["jwis"],
    version="0.3.0",
    description="Data downloader from Japan Water System Information",
    author="Kiwamu Ishikura",
    author_email="ishikura.kiwamu@gmail.com",
    url="https://github.org/i-kiwamu/jwis",
    keywords=["download", "hydrology", "japan"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: Japanese",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
        ],
    long_description="""\
=========================================================
jwis: Data downloader from Japan Water Information System
=========================================================

- Author: Kiwamu Ishikura
- Licence: GPLv3

What's this?
------------
This is a program to get hydrological data from `Water Information System`_
provided from Japanese Ministry of Land, Infrastructure, Transport and Tourism.
You can retrieve data and, save as csv. *Only water level and flow rate data
are available*, because this program is still in beta version.

.. _`Water Information System`: http://www1.river.go.jp/

Requirements
------------
- Python (>= 2.7 or >= 3.3)
- pandas (>= 0.18.0)


Installation
------------
If you have pip, you can install by pip as below::

    $ pip install jwis

Or, you can install by setup.py::

    $ python setup.py install

Usage
-----
Just type as below in your console::

    $ jwis

Program will ask you the beginning and final date you want, observatory ID
(観測所記号), and file name. Please follow the explanations.
""",
    **params
)

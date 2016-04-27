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
    name = "jwis",
    packages = ["jwis"],
    version = "0.1.0",
    description = "Data downloader from Japan Water System Information",
    author = "Kiwamu Ishikura",
    author_email = "ishikura.kiwamu@gmail.com",
    url = "https://github.org/i-kiwamu/jwis",
    keywords = ["download", "hydrology", "japan"],
    classifiers = [
        "Programming Language :: Python",
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
    long_description = """\
jwis: Data downloader from Japan Water Information System
=========================================================

* Author: Kiwamu Ishikura
* Version: 0.1.0
* Licence: GPLv3

What's this?
------------
This is a program to get hydrological data from Water Information System provided from Japanese Ministry of Land, Infrastructure, Transport and Tourism (http://www1.river.go.jp/). You can retrieve data and save as csv.

Requirement
-----------
Python (>= 3.3)
*Beware that Python 2 can NOT work*

Usage
-----
Download jwis, and you can type the followings on your console::

```
$ python3 jwis.py
```

Program will ask you the beginning/final date of data you want, locations, and file name. Please follow the explanations.

If you put jwislib.py in your PYTHONLIB and put jwis.py in your PATH, you can use these program anywhere.
""",
    **params
)

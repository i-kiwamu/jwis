jwis: Data downloader from Japan Water Information System
=========================================================

* Author: Kiwamu Ishikura
* Licence: GPLv3

[![PyPI version](https://badge.fury.io/py/jwis.svg)](https://badge.fury.io/py/jwis)

What's this?
------------
This is a program to get hydrological data from Water Information System provided from Japanese Ministry of Land, Infrastructure, Transport and Tourism (http://www1.river.go.jp/). You can retrieve data and save as csv.

Requirement
-----------
* Python (>= 3.3)
* pandas (>= 0.18.0)
*Beware that Python 2 can NOT work*

Installation
------------
If you have pip, you can install by pip as follows::

```
$ pip install jwis
```

Or, you can install by setup.py

```
$ python3 setup.py install
```

Usage
-----
Just type as follows in your console

```
$ jwis
```

Program will ask you the beginning/final date of data you want, observatory ID, and file name. Please follow the explanations.

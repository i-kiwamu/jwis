jwis: Data downloader from Japan Water Information System
=========================================================

* Author: Kiwamu Ishikura
* Licence: GPLv3

[![PyPI version](https://badge.fury.io/py/jwis.svg)](https://badge.fury.io/py/jwis)

What's this?
------------
This is a program to get hydrological data from [Water Information System](http://www1.river.go.jp/) provided from Japanese Ministry of Land, Infrastructure, Transport and Tourism. You can retrieve data and, save as csv. *Only water level and flow rate data are available*, because this program is still in beta version.

Requirements
------------
* Python (>= 2.7 or >= 3.3)
* pandas (>= 0.18.0)

Installation
------------
If you have pip, you can install by pip as below

```
$ pip install jwis
```

Or, you can install by setup.py

```
$ python setup.py install
```

Usage
-----
Just type as below in your console

```
$ jwis
```

Program will ask you the beginning and final date you want, observatory ID (観測所記号), and file name. Please follow the explanations.

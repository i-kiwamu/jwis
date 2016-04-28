#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, timedelta
import sys
import pandas as pd
import codecs
from .jwislib import JWIS

sys_encoding = sys.stdout.encoding

try:
   input = raw_input
except NameError:
   pass

def ask_date():
    print("Beginning date")
    d_start_year = int(input("    year? "))
    d_start_month = int(input("    month? "))
    d_start_date = int(input("    date? "))
    d_start = date(d_start_year, d_start_month, d_start_date)

    print("Final date")
    d_end_year = int(input("    year? "))
    d_end_month = int(input("    month? "))
    d_end_date = int(input("    date? "))
    d_end = date(d_end_year, d_end_month, d_end_date)

    return (d_start, d_end)

def ask_observatory():
    obs_id = input("Type observatory ID: ")
    return obs_id

def main():
    date_periods = ask_date()
    d_start = date_periods[0]
    d_end = date_periods[1]
    if d_start > d_end:
        d_start, d_end = d_end, d_start

    obs_id = ask_observatory()

    output_filename = input("saving file name? ")
    jwis = JWIS(obs_id, d_start, d_end, "NO")
    jwis_table = jwis.retrieve_hq_data()
    jwis_table.to_csv(output_filename)
    print("Done")

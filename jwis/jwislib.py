# -*- coding: utf-8 -*-

# ------------------------------------------------
# jwislib
#   read & write data from Japan Water Information System
# ------------------------------------------------

try:
    from urllib.request import urlopen
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlopen, urlencode
import datetime
import pandas as pd
from .JWISHTMLParser import JWISParser

class JWIS:
    def __init__(self, obs_id, date_begin, date_end, kawabou):
        self.view_url = "http://www1.river.go.jp/cgi-bin/DspWaterData.exe"
        self.obs_id = obs_id
        self.date_begin = date_begin
        self.date_end = date_end
        self.kawabou = kawabou

    def kind_name(self, kind):
        if kind == '1':
            return 'H'
        elif kind == '5':
            return 'Q'
        else:
            return 'X'

    def retrieve_data(self, kind):
        kn = self.kind_name(kind)
        columns = ["Date", "Time", kn, "Flag_" + kn]
        data = pd.DataFrame(columns=columns)

        url_params_dict = {
            "KIND": kind,
            "ID": self.obs_id,
            "KAWABOU": self.kawabou
        }

        d = self.date_begin
        while d <= self.date_end:
            date_delta = min(datetime.timedelta(days=30), self.date_end - d)
            d1 = d + date_delta
            url_params_dict["BGNDATE"] = d.strftime("%Y%m%d")
            url_params_dict["ENDDATE"] = d1.strftime("%Y%m%d")
            url_params = urlencode(url_params_dict)
            view_uri = self.view_url + '?' + url_params
            f = urlopen(view_uri)

            parser = JWISParser()
            parser.feed(f.read().decode("euc-jp"))
            parser.close()

            data_list = []
            # with urlopen(parser.data_url) as data_file:
            data_file = urlopen(parser.data_url)
            for line in data_file:
                line = line.decode("Shift_JIS")
                if line.count(',') == 3 and not line.startswith('#'):
                    data_list.append(line.rstrip("\r\n").split(','))

            data = data.append(pd.DataFrame(data_list, columns=columns))
            d = d1 + datetime.timedelta(days=1)
        return data

    def retrieve_hq_data(self):
        h_data = self.retrieve_data('1')
        q_data = self.retrieve_data('5')
        hq_data = pd.merge(h_data, q_data, on=["Date", "Time"], how="outer")
        return hq_data

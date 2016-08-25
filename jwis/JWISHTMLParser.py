# -*- coding: utf-8 -*-

# ------------------------------------------------
# JWISHTMLParser
#   HTML Parser for Japan Water Information System
# ------------------------------------------------

try:
    from urllib.parse import parse_qs
    from html.parser import HTMLParser
except ImportError:
    from urlparse import parse_qs
    from HTMLParser import HTMLParser


class JWISParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.host = "http://www1.river.go.jp"

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attrs_dict = dict(attrs)
            url = attrs_dict["href"]
            if url.startswith("/dat/dload/download"):
                self.data_url = self.host + url

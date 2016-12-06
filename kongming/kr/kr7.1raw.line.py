#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import ckr
import HTMLParser

rec = {}

def init():
    rec["1"] = ""

def save(an):
    if not (rec["1"] == ""):
        print an + "\t" + rec["1"]
        init()

if __name__ == "__main__":
    an = ""
    init()
    for line in sys.stdin:
#        html_parser = HTMLParser.HTMLParser()
#        line = html_parser.unescape(line)

        line = line.strip();
        items = line.split("\t")

        if len(items) == 2:
            if line.startswith("Url:http://www"):
                save(an)
                an = ckr.getpn(line)
            else:
               if items[0] == "1":
                   rec["1"] = items[1]
                   save(an)

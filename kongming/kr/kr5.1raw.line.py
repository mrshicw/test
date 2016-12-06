#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re
import json
import ckr
import HTMLParser

record = {}
rec = {}

def init():
    rec["1"] = ""
    rec["2"] = ""
    rec["3"] = ""

def save(an):
	if not (rec["1"] == "" and rec["2"] == "" and rec["3"] == ""):
            print an + "\t" + rec["1"] + "\t" + rec["2"] + "\t" + rec["3"]
        init()

if __name__ == "__main__":
    an = ""
    init()
    for line in sys.stdin:
        html_parser = HTMLParser.HTMLParser()
        line = html_parser.unescape(line)

        line = line.strip();
        items = line.split("\t")

        if len(items) == 2:
            if line.startswith("Url:http://www"):
                save(an)
                an = ckr.getpn(line)
            else:
               if items[0] == "1":
                   save(an)
                   rec["1"] = items[1]
               elif items[0] == "2":
                   rec["2"] = items[1]
               elif items[0] == "3":
                   rec["3"] = items[1]
                   save(an)
    save(an)

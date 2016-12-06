#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import HTMLParser
import re
import json
import ckr
rec = {}
ty = ""

def init():
    rec["1"] = ""
    rec["2"] = ""
    rec["3"] = ""
    rec["4"] = ""

def save(ty, an):
	if not (rec["1"] == "" and rec["2"] == "" and rec["3"] == "" and rec["4"] == ""):
            print an + "\t" + ty + "\t" + rec["1"] + "\t" + rec["2"] + "\t" + rec["3"] + "\t" + rec["4"]
         
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
                save(ty, an)
                an = ckr.getpn(line)
                
            else:
               types = items[0].split(".")
               ty = types[0]
               if types[1] == "1":
                   save(ty, an)
                   rec["1"] = items[1]
               elif types[1] == "2":
                   rec["2"] = items[1]
               elif types[1] == "3":
                   rec["3"] = items[1]
               elif types[1] == "4":
                   rec["4"] = items[1]
                   save(ty, an)
    save(ty, an)

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import ckr
import HTMLParser

rec = {}

def save(pn):

    if not (rec["1"] == "" and rec["2"] == "" and rec["3"] == "" and rec["4"] == "" and rec["5"] == ""):
        print pn + "\t" + rec["1"] + "\t" + rec["2"] + "\t" + rec["3"] + "\t" + rec["4"] + "\t" + rec["5"]
    ckr.init(rec, 5)


if __name__ == "__main__":
    pn = ""
    ckr.init(rec, 5)

    for line in sys.stdin:
        html_parser = HTMLParser.HTMLParser()
        line = html_parser.unescape(line)

        line = line.strip();
        items = line.split("\t")

        if len(items) == 2:
            if line.startswith("Url:http://www"):
                pn = ckr.getpn(line)
                save(pn)
            else:
               if items[0] == "1":
                   save(pn)
                   rec["1"] = items[1]
               elif items[0] == "2":
                   rec["2"] = items[1]
               elif items[0] == "3":
                   rec["3"] = items[1]
               elif items[0] == "4":
                   rec["4"] = items[1]
               elif items[0] == "5":
                   rec["5"] = items[1]
                   save(pn)
        else:
            pass

    save(pn)

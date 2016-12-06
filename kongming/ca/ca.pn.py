#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import HTMLParser

if __name__ == "__main__":
    pn = ""
    PN = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "PN":
                pn = value.replace(" ", "")

            if PN == "":
                PN = pn
            elif PN == pn:
                if field != "PN":
                    print line
            elif PN != pn:
                print "PN" + "\t" + PN
                PN = pn
        else:
            pass
    print "PN" + "\t" + PN

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
                pn = value

            if PN == "":
                PN = pn

            if PN != pn:
                PN = pn

            print PN + "\t" + field + "\t" + value            
        else:
            pass
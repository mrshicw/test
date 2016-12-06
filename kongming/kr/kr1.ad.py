#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        key, field = items[0], items[1]
        if field.startswith("(21) Application No.(Date)"):
            value = field.replace("(21) Application No.(Date)", "")
            terms = value.split("(")
            ad = terms[-1]
            ad = ad.replace(".", "")
            ad = ad.replace(")", "")
            print key + "\t" + "AD" + "\t" + ad
        else:
            print line

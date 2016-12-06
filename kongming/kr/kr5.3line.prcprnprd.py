#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re

def save_multi(value, term):
    if value == "":
        value = term
    else:
        value = value + ";" + term
    return value

if __name__ == "__main__":
    key, field, value = "", "", ""
    prc, prn, prd = "", "", ""
    for line in sys.stdin:
        line = line.strip();
        items = line.split("\t")
        if len(items) > 2:
            key, field, value = items[0], items[1], items[2]
            terms = value.split(";")
            for term in terms:
                segs = term.split(" ")
                if len(segs) == 3:
                    prc = save_multi(prc, segs[0])
                    prn = save_multi(prn, segs[1])
                    prd = save_multi(prd, segs[2])
                else:
                    pass
                    #sys.stderr("not 3 segs : " + line)
        print line
        if prc != "":
            print key + "\t" + "PRC" + "\t" + prc
            print key + "\t" + "PRN" + "\t" + prn
            print key + "\t" + "PRD" + "\t" + prd
        
        prc, prn, prd = "", "", ""

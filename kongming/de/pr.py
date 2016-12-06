#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def save_multi(value, term):
    if value == "":
        value = term
    else:
        value = value + ";" + term
    return value

def pr(field, value):
    prc, prn, prd = "", "", ""
    terms = value.split(";")
    for term in terms:
        segs = term.split(" ")
        if len(segs) == 3:
            prc = save_multi(prc, segs[0])
            prn = save_multi(prn, segs[1])
            prd = save_multi(prd, segs[2])
        else:
            pass

    print "PR" + "\t" + value
    if prc != "":
        print "PRC" + "\t" + prc
        print "PRN" + "\t" + prn
        print "PRD" + "\t" + prd
        

if __name__ == "__main__":
    key, field, value = "", "", ""
    for line in sys.stdin:
        line = line.strip();
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "PR":
                pr(field, value)
            else:
                print line

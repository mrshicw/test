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

def ian(key, field, value, line):
    ianc, iann, iand = "", "", ""
    terms = value.split(";")
    for term in terms:
        segs = term.split(" ")
        if len(segs) == 3:
            ianc = save_multi(ianc, segs[0])
            iann = save_multi(iann, segs[1])
            iand = save_multi(iand, segs[2])
        else:
            pass
            #sys.stderr("not 3 segs : " + line)

    print line
    if ianc != "":
        print key + "\t" + "IANC" + "\t" + ianc
        print key + "\t" + "IANN" + "\t" + iann
        print key + "\t" + "IAND" + "\t" + iand
        

def ipn(key, field, value, line):
    ipnc, ipnn, ipnd = "", "", ""
    terms = value.split(";")
    for term in terms:
        segs = term.split(" ")
        if len(segs) == 3:
            ipnc = save_multi(ipnc, segs[0])
            ipnn = save_multi(ipnn, segs[1])
            ipnd = save_multi(ipnd, segs[2])
        else:
            pass
            #sys.stderr("not 3 segs : " + line)

    print line
    if ipnc != "":
        print key + "\t" + "IPNC" + "\t" + ipnc
        print key + "\t" + "IPNN" + "\t" + ipnn
        print key + "\t" + "IPND" + "\t" + ipnd
        

def pr(key, field, value, line):
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
            #sys.stderr("not 3 segs : " + line)

    print line
    if prc != "":
        print key + "\t" + "PRC" + "\t" + prc
        print key + "\t" + "PRN" + "\t" + prn
        print key + "\t" + "PRD" + "\t" + prd
        

if __name__ == "__main__":
    key, field, value = "", "", ""
    prc, prn, prd = "", "", ""
    for line in sys.stdin:
        line = line.strip();
        items = line.split("\t")
        if len(items) > 2:
            key, field, value = items[0], items[1], items[2]
            if field == "PR":
                pr(key, field, value, line)
            elif field == "IAN":
                ian(key, field, value, line)
            elif field == "IPN":
                ipn(key, field, value, line)
            else:
                print line

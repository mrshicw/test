#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)

if __name__ == "__main__":
    dictpn = {}
    dictpd = {}

    f = open(sys.argv[1])
    for line in f:
        line = line.strip()
        items = line.split("\t")
        
        key = items[0]
        value = items[1]
        
        segs = value.split("|")
        if segs[0] != "" and segs[1] != "":
            dictpn[key] = segs[0]
            dictpd[key] = segs[1]
    f.close()

    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        key, field, value = items[0], items[1], items[2]

        if key in dictpn:
            pn = dictpn[key]
            pd = dictpd[key]

            print pn + "\t" + field + "\t" + value

            if field == "AN":
                print pn + "\t" + "PN" + "\t" + pn
                print pn + "\t" + "PD" + "\t" + pd



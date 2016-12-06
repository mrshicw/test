#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    KEY = ["AB.EN", "AB.FR", "AD", "AGC", "AN", "AU", "CAC", "GA", "IAND", "IANN", "IPCR", "IPND", "IPNN", "PA", "PA.2", "PCTF", "PD.1", "PD.2", "PN", "PRC", "PRN", "PRD", "SCRQ", "SQYY", "TI.EN", "TI.FR", "XKDYXX"]
    for line in sys.stdin :
        line = line.strip()
        items = line.split("\t")
        key = items[0]
        key = key.replace(" ", "")

        if len(items) == 1 and (not line.startswith("0000000000")):
            if key in KEY :
                print "\n" + line  + "\t",
            else:
                print " " + line,
            
        if len(items) == 2  and (not line.startswith("0000000000")):
            print "\n" + line,

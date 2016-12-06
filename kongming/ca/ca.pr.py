#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    pn = ""
    PN = ""
    list = []
    pr = ""
    prc = ""
    prn = ""
    prd = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            value = value.strip()

            if field == "PRN":
                pr = value
                if prn == "":
                    prn = value
                else:
                    prn = prn + ";" + value
            if field == "PRC":
                pr = value + " " + pr
                if prc == "":
                    prc = value
                else:
                    prc = prc + ";" + value
            if field == "PRD":
                pr = pr + " " + value
                list.append(pr)
                pr = ""
                if prd == "":
                    prd = value
                else:
                    prd = prd + ";" + value

            if not(field == "PN" or field == "PRC" or field == "PRN" or field == "PRD"):
                print line

            # 遇到PN，本单元结束
            if field == "PN":
                pr = ";".join(list)
                if pr != "":
                    print "PRC" + "\t" + prc
                    print "PRN" + "\t" + prn
                    print "PRD" + "\t" + prd
                    print "PR" + "\t" + pr
                print line

                pr = ""
                list = []
                prc = ""
                prn = ""
                prd = ""

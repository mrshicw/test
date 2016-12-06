#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    pn = ""
    PN = ""
    ctd = ""

    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]

            if field == "CTNP":
                if ctd == "":
                    ctd = value
                else:
                    ctd = ctd + ";"  + value

            # 遇到PN，本单元结束
            if field == "PN":
                if ctd != "":
                    ctd = ctd.replace(" \x01", ";")
                    ctd = ctd.replace("\x01", ";")
                    print "CTD" + "\t" + ctd
                    ctd = ""
                print line
            else:
                print line

    if ctd != "":
        ctd = ctd.replace(" \x01", ";")
        ctd = ctd.replace("\x01", ";")
        print "CTD" + "\t" + ctd

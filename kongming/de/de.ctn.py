#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    pn = ""
    PN = ""
    ctn = ""

    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]

            if field == "CT":
                if ctn == "":
                    ctn = value
                else:
                    ctn = ctn + ";"  + value

            # 遇到PN，本单元结束
            if field == "PN":
                if ctn != "":
                    ctn = ctn.replace(" \x01", ";")
                    ctn = ctn.replace("\x01", ";")
                    ctn = ctn.replace(" ", ";")
                    print "CTN" + "\t" + ctn
                    ctn = ""
                print line
            else:
                print line

    if ctn != "":
        ctn = ctn.replace(" \x01", ";")
        ctn = ctn.replace("\x01", ";")
        ctn = ctn.replace(" ", ";")
        print "CTN" + "\t" + ctn

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    pn = ""
    PN = ""
    icm = ""
    ics = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            # 取第一个
            if field == "ICM":
                items = value.split(";")
                icm = items[0]
            # 全取
            if field == "ICS":
                items = value.split(" \x01")
                value = ";".join(items)
                ics = value
            # 遇到PN，本单元结束
            if field == "PN":
                value = icm + ";" + ics
                if value != ";":
                    print "IPC" + "\t" + value
                    icm = ""
                    ics = ""
                print line
            else:
                print line

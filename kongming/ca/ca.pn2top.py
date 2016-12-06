#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def out(key, field, value):
    if value != "":
        print key + "\t" + field + "\t" + value

if __name__ == "__main__":
    data = ""
    for line in sys.stdin:
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            # 遇到PN，本单元结束
            if field == "PN":
                print line,
                print "AC" + "\t" + "CA"
                print data,
                data = ""
            else:
                data = data + line

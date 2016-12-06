#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    list = []
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "AB":
                value = value.replace(";CT ", "\nCTN\t")
                print field + "\t" + value
            else:
                print line
        elif len(items) == 3:
            key, field, value = items[0], items[1], items[2]
            if field == "AB":
                value = value.replace(";CT \x01", "\n" + key + "\t" + "CTN\t")
                print key + "\t" + field + "\t" + value
            pass

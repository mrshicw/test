#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        line = line.replace("PRC \x01PRN \x01PRD", "PR")
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            field = field.replace(" ", "")
            field = field.replace("\x01", "")
            print field + "\t" + value

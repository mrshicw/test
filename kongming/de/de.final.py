#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    de = ["AC", "AN", "AD", "PD", "PN", "TI", "AB", "PA", "AU", "ADDR", "PR", "PRC", "PRN", "PRD", "IPC", "CTN", "CTD"]
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field in de:
                print line

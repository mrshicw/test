#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "AC":
                value = value.replace(" ", "")
                value = value.replace("PR", "")
                print field + "\t" + value
            else:
                print line
                
        else:
            print line


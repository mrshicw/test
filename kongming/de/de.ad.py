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
            if field == "AD":
                items = value.split(".")
                if len(items) == 3:
                    value = items[2] + items[1] + items[0]
                    value = value.replace(" ", "")
                    value = value.replace("PR", "")
                    print field + "\t" + value
                else:
                    pass
            else:
                print line

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 3:
            key, field, value = items[0], items[1], items[2]
            value = value.strip()

            if not ( len(value) <= 5 or value.startswith("Content none") or value.startswith("The content none") ):
                print line
        else:
            print line

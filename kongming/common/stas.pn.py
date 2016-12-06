#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    dict = {}
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) > 2:
            key = items[0]
            if key not in dict:
                dict[key] = key

    for key in dict:
        print key

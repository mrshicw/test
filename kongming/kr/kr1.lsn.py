#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        key, field = items[0], items[1]
        if field.startswith("Final administrative status"):
            value = field.replace("Final administrative status", "")
            value =  re.sub(r'(\(.+?\))', "", value)
            print key + "\t" + "LSN" + "\t" + value
        else:
            print line

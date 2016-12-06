#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def run(field, value):
# 优先选择英文
    items = value.split("[EN] ")

    if len(items) == 2:
        value = items[1]
    else:
        value = items[0].replace("[DE] ", "")
    value = value.replace("[null] ", "")
    field = field.strip()
    value = value.strip()
    return field + "\t" + value

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "TI" or field == "AB":
                line = run(field, value)
                print line
            else:
                print line

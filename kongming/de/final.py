#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)

def val_format(value):
    list = []
    items = value.split(";")
    for item in items:
        item = item.strip()
        if item != None:
            if item != "" :
                list.append(item)
    value = ";".join(list)
    value = value.replace("  ", " ")
    return value

def run(line):
    line = line.strip();
    items = line.split("\t")

    if len(items) == 3:
        key, field, value = items[0], items[1], items[2]
        value = val_format(value)
        return key + "\t" + field + "\t" + value
        
if __name__ == "__main__":
    for line in sys.stdin:
        line = run(line)
        if line != None:
            print line

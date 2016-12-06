#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)

def getAddr(line):
    items = line.split(" /")
    if len(items) == 2:
        return items[1]

def getTime(line):
    items = line.split("/")
    return items[-3]

def getName(line):
    items = line.split("/")
    return items[-1]

def getPn(line):
    items = line.split(".")
    return items[0]

if __name__ == "__main__":
    dict_addr = {}
#统计行，到字典
    for line in sys.stdin:
        line = line.strip()
        pn = getName(line)

        if pn in dict_addr and line > dict_addr[pn]:
            dict_addr[pn] = line
        else:
            dict_addr[pn] = line
#输出字典
    for key in dict_addr:
        print dict_addr[key]

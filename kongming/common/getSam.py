#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)


def getAddr(line):
    items = line.split(" /")
    if len(items) == 2:
        return items[1]

def getName(line):
    items = line.split("/")
    return items[-1]

def getPn(line):
    items = line.split(".")
    return items[0]

def load(file):
    dict = {}
    f = open(file)
    for line in f:
        line = line.strip()
        dict[line] = line
    return dict

if __name__ == "__main__":
    file = sys.argv[1]
    dict = load(file)

    for line in sys.stdin:
        line = line.strip()
        name = getName(line)
        pn = getPn(name)
        if pn in dict:
            print line

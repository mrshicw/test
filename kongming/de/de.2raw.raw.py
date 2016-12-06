#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def getPN(line):
    items = line.strip().split("\t")
    tmp = items[0].split("/")
    f = tmp[len(tmp) - 1]
    files = f.split(".")
    return files[0]

def get(line):
    line = line.strip()
    items = line.split("\t")
    if len(items) == 2:
       print "\n" + line,
    elif len(items) == 1:
       if len(line) > 10:
           if "PRC" in line:
               print line
           else:
               print ";" + line,


if __name__ == "__main__":
    for line in sys.stdin:
        get(line)

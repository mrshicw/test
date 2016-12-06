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
    if line.startswith("Url:http://www"):
#        print "\n" + "PN" + "\t" + getPN(line),
        pass
    else :
        line = line.strip()
        if line.startswith("3\t"):
            items = line.split("\t")
            if len(items) == 2:
                print "\n" + items[1],
        elif line.startswith("4\t"):
            items = line.split("\t")
            if len(items) == 2:
                print "\t" + items[1],
        elif line.startswith("PN"):
            items = line.split("\t")
            if len(items) == 2:
                field = items[0]
                value = items[1]
                value = value.replace("Dokument", "")
                value = value.replace(" ", "")
                values = value.split("(")
                value = values[0]
                print "\n" + "PN" + "\t" + value,
        elif line == "3":
            pass
        elif line == "4":
            pass
        elif line == "":
            pass
        else:
            print "\x01" + line,
        
if __name__ == "__main__":
    for line in sys.stdin:
        get(line)

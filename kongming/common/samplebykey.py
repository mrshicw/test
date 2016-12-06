#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")


#输入字典列表，按照key抽样
def load(file):
    list = []
    f = open(file)
    for line in f:
        line = line.strip()
        items = line.split("\t")
        line  = items[0]
        list.append(line)
    f.close()
    return list


if __name__ == "__main__":
    N = 0
    file = sys.argv[1]
    list = load(file)
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) > 2:
            key = items[0]
            if key in list:
                print line

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

##抽样100，输入文件名，输出打印

#间隔指定行打印文本

if __name__ == "__main__":
    f = open(sys.argv[1])
    dict = {}
    for line in f:
        line = line.strip()
        items = line.split("\t")
        if len(items) > 2:
            key = items[0]
            dict[key] = key
    f.close()


    N = len(dict)
    n = N / 100
    count = 0
    dict2 = {}
    for key in dict:
        if count % n == 0:
            dict2[key] = key
        count = count + 1

    f = open(sys.argv[1])
    for line in f:
        line = line.strip()
        items = line.split("\t")
        if len(items) > 2:
            key = items[0]
            if key in dict2:
                print line
    f.close()

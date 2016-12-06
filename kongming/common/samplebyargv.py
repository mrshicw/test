#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

##抽样程序

#间隔指定行打印文本

#输入一个参数，为每隔几个进行抽样
if __name__ == "__main__":
    N = 0
    sam = int(sys.argv[1])

    for line in sys.stdin:
        if (N % sam) == 0:
            print line,
        N = N + 1

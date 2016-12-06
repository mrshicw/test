#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
num_ls = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
if __name__ == "__main__":
    an = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field = items[0]
            value = items[1]
            if field == "AN":
                an = value
                print an + "\t" + "AN" + "\t" + "KR" + value
            else:
                if field in num_ls:
                    print an + "\t" + value
                else:
                    print an + "\t" + line

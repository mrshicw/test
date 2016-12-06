#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    dir = ""

    print "#bin"
    for line in sys.stdin:
        line = line.strip()
        items = line.split("/")
        file = items[-1]
        files = file.split(".")
        key = files[0]

        length = len(key)

        if length <= 4:
            dir = str(key)
        elif length > 4 and length <= 8:
            dir = str(key[0 : 4]) + "/" + str(key[4 : -1])
        elif length > 8 and length <= 11:
            dir = str(key[0 : 4]) + "/" + str(key[4 : 8]) + "/" + str(key[8 : -1])
        else:
            dir = str(key[0 : 4]) + "/" + str(key[4 : 8]) + "/" + str(key[8 : 11]) + "/" + str(key[11 : -1])

        print "mkdir -p " + "/data/d0/data_html/kr/" + dir

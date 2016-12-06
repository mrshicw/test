#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def getdir(an):
    dir = ""
    length = len(an)

    if length <= 5:
        dir = "000000"
    elif length > 5 and length <= 10:
        dir = str(an[0 : 5])
    elif length > 10 and length <= 14:
        dir = str(an[0 : 5]) + "/" + str(an[5 : 10])
    else:
        dir = str(an[0 : 5]) + "/" + str(an[5 : 10]) + "/" + str(an[10 : 14])
    return "/data/d0/data_data/kr/" + dir

if __name__ == "__main__":
    dict = {}
    print "#bin"
    for line in sys.stdin:
        line = line.strip()

        items = line.split("/")
        an = items[-1]
        an = an.replace(".1", "")

        dir = getdir(an)
        dict[dir] = dir

    for key in dict:
        print "mkdir -p " + key

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("Url:http://www"):
            items = line.split("\t")
            terms = items[0].split("/")
            tmp = terms[-1]
            an = tmp.replace(".1", "")

            print "AN" + "\t" + str(an)
#            print "AN" + "\t" + "KR" + str(an)
        else:
            print line

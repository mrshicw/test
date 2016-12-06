#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
prc_dic = {}

def prc(value):
    for abr in prc_dic:
        if abr in value:
            value = value.replace(abr, prc_dic[abr])
    for abr in prc_dic:
       if abr in value:
            value = value.replace(abr, prc_dic[abr])
    value = value.replace("Germany", "DE")
    value = value.replace(" ", "")
    return value

if __name__ == "__main__":
    f = open(sys.argv[1])
    for line in f.readlines():
        items = line.strip().split("\t")
        if len(items) == 2:
            prc_dic[items[1]] = items[0]
    f.close()

    pn = ""
    PN = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "PRC":
                value = prc(value)
                value = value.replace("Republicof", "")
                value = value.replace("DemocraticPeople's", "")
                print field + "\t" + value
            else:
                print line
        else:
            pass

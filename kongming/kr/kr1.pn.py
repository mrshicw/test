#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def getpnpd(value):
    items = value.split("(")
    pn = ""
    pd = ""    
    if len(items) == 1:
        pd = items[-1]
    if len(items) == 2:
        pn = "KR" + str(items[0])
        pd = items[1]

    pd = pd.replace(".", "")
    pd = pd.replace(")", "")

    return pn, pd

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        key, field = items[0], items[1]
        if field.startswith("(11) Registration No.(Date)"):
            value = field.replace("(11) Registration No.(Date)", "")
           
        else:
            print line

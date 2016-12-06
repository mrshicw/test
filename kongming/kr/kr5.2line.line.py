#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re
import json
import ckr

def saveline(prd, prc, prn):
    tmp = prd.split("(")
    prd = tmp[-1].replace(")", "")
    prn = prn.replace(".", "")
    return prd + " " + prc + " " + prn

if __name__ == "__main__":
    AN = ""
    value = ""
    for line in sys.stdin:
        line = line.strip();
        items = line.split("\t")
        if len(items) == 4:
            an, prd, prc, prn = items[0], items[1], items[2], items[3]

            if AN == "":
                AN = an
                value = saveline(prd, prc, prn)
            elif AN == an:
                term = saveline(prd, prc, prn)
                if value == "":
                    value = term
                else:
                    value = value + ";" + term
            elif AN != an:
                value =  re.sub(r'(\(.+?\))', "", value)
                print AN + "\t" + "PR" + "\t" + value
                value = ""

                AN = an
                term = saveline(prd, prc, prn)
                if value == "":
                    value = term
                else:
                    value = value + ";" + term

    print AN + "\t" + "PR" + "\t" + value

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    list = []
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "PR":
                items = value.split(";")
                for item in items:
                    terms = item.split("\x01")
                    if len(terms) == 3:
                        prc, prn, prd = terms[0], terms[1], terms[2]
                        prc = prc.strip()
                        prn = prn.strip()
                        prd = prd.strip()
                        list.append(prc + " " + prn + " " + prd)
                    else:
                        pass
                value = ";".join(list)
                value = value.replace(";CT ", "\nCTN\t")
                print field + "\t" + value
                list = []
            else:
                print line
        else:
            pass

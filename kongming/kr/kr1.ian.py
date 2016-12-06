#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        key, field = items[0], items[1]
        if field.startswith("(86) Int'l Application No.(Date)"):
            value = field.replace("(86) Int'l Application No.(Date)", "")

            ianc = ""
            iann = ""
            iand = ""
            value = value.replace(")", "")
            values = value.split("(")
            if len(values) == 2:
                iann = values[0]
                terms = iann.split("/")
                if len(terms) > 1:
                    term = terms[1]
                    if len(term) > 3:
                       ianc = term[0] + term[1]
                       if "A" <= term[2] and term[2] < "Z":
                           ianc = ianc + term[2]

                iand = values[1].replace(".", "")

            if ianc != "":
                print key + "\t" + "IAN" + "\t" + ianc + " " + iann + " " + iand
                print key + "\t" + "IANC" + "\t" + ianc
                print key + "\t" + "IANN" + "\t" + iann
                print key + "\t" + "IAND" + "\t" + iand
        else:
            print line

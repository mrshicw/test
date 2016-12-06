#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
def IANC(value):
    terms = value.split("/")
    if len(terms) > 1:
        term = terms[1]
        if len(term) > 3:
            c = term[0] + term[1]
            if "A" <= term[2] and term[2] < "Z":
                c = c + term[2]
    return c

if __name__ == "__main__":
    pn = ""
    PN = ""
    ad = ""
    iann = ""
    iand = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            value = value.strip()

            if field == "AD":
                ad = value
            if field == "IANN":
                iann = value
            if field == "IAND":
                iand = value

            if not (field == "PN" or field == "AD" or field == "IANN" or field == "IAND") :
                print line

            # 遇到PN，本单元结束
            if field == "PN":
                ad = ad.replace("-", "")
                iann = iann.replace(" ", "")
                iand = iand.replace("-", "")

                if ad == "":
                    ad = iand
                if ad != "":
                    print "AD" + "\t" + ad
                if iann != "":
                    if iand == "":
                        iand = ad
                    print "IANC" + "\t" + IANC(iann)
                    print "IANN" + "\t" + iann
                    print "IAND" + "\t" + iand
                    print "IAN" + "\t" + IANC(iann) + " " + iann + " " + iand
                print line

                ad = ""
                iann = ""
                iand = ""

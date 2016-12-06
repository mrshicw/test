#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def save_multi(value, term):
    if value == "":
        value = term
    else:
        value = value + ";" + term
    return value

def ian_ipn_pr(value):
    list = []
    vc, vn, vd = "", "", ""
    terms = value.split(";")
    for term in terms:
        segs = term.split(" ")
        if len(segs) == 3:
            vc = save_multi(vc, segs[0])
            vn = save_multi(vn, segs[1])
            vd = save_multi(vd, segs[2])
        else:
            pass

    list.append(value)
    list.append(vc)
    list.append(vn)
    list.append(vd)

    return list

if __name__ == "__main__":
    key, field, value = "", "", ""
    for line in sys.stdin:
        line = line.strip();
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "IAN":
                list = ian_ipn_pr(value)
                print "IAN" + "\t" + list[0]
                print "IANC" + "\t" + list[1]
                print "IANN" + "\t" + list[2]
                print "IAND" + "\t" + list[3]
            else:
                print line
        elif len(items) == 3:
            key, field, value = items[0], items[1], items[2]
            if field == "IAN":
                list = ian_ipn_pr(value)
                print key + "\t" + "IAN" + "\t" + list[0]
                print key + "\t" + "IANC" + "\t" + list[1]
                print key + "\t" + "IANN" + "\t" + list[2]
                print key + "\t" + "IAND" + "\t" + list[3]
            else:
                print line

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import json


def saveline(lse, lsd, lsi):
    dic = {}
    lsd = lsd.replace(".", "")
    dic["LSE"] = lse
    dic["LSD"] = lsd
    dic["LSI"] = lsi
    return dic

if __name__ == "__main__":
    AN = ""
    an = ""
    list = []
    for line in sys.stdin:
        line = line.strip();
        items = line.split("\t")
        an = items[0]

        if len(items) == 6:
            lse, lsd, lsi = items[2], items[3], items[4]
            if AN == "":
                AN = an
                list.append(saveline(lse, lsd, lsi))
            elif AN == an:
                list.append(saveline(lse, lsd, lsi))
            elif AN != an:
                value = json.dumps(list, ensure_ascii=False)
                print AN + "\t" + "LE" + "\t" + value

                AN = an
                list = []
                list.append(saveline(lse, lsd, lsi))

    value = json.dumps(list, ensure_ascii=False)
    print AN + "\t" + "LE" + "\t" + value

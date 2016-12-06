#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re
import json
import ckr

def saveline(no, cont):
    dic = {}
    dic["no"] = no
    dic["cont"] = cont
    return dic

if __name__ == "__main__":
    AN = ""
    list = []
    for line in sys.stdin:
        line = line.strip();
        items = line.split("\t")
        an = items[0]
        if len(items) == 3:
            no, cont = items[1], items[2]
            if AN == "":
                AN =an
                list.append(saveline(no, cont))
            elif AN == an:
                list.append(saveline(no, cont))
            elif AN != an:
                value = json.dumps(list, ensure_ascii=False)
                print AN + "\t" + "CLM" + "\t" + value

                AN = an
                list = []
                list.append(saveline(no, cont))

    value = json.dumps(list, ensure_ascii=False)
    print AN + "\t" + "CLM" + "\t" + value

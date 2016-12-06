#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import ckr


def CTN(value):
    list = []
    value = value.replace("::Empty::", "")
    items = value.split("&nbsp;")
    for item in items:
        if item != "":
            list.append(item)
    value = ";".join(list)
    return value

if __name__ == "__main__":
    AN = ""
    value = ""

    for line in sys.stdin:
        line = line.strip()
        line = line.replace("*", "")
        items = line.split("\t")
        if len(items) == 2:
            an, ctn = items[0], items[1]
            ctn = ctn.replace(" ", "")
            ctn = CTN(ctn)
            if AN == "":
                AN = an
                value = ctn
            elif AN == an:
                if value == "":
                    value = ctn
                else:
                    value = value + ";" + ctn
            elif AN != an:
                if value != "":
                    print AN + "\t" + "CTN" + "\t" + value
                value = ""

                AN = an
                if value == "":
                    value = ctn
                else:
                    value = value + ";" + ctn

    if value != "":
        print AN + "\t" + "CTN" + "\t" + value

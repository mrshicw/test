#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import json
import ckr

def saveline(ty, au, cty, addr):
    if ty == "1":
        ckr.save2json(record, "PA", au)
        ckr.save2json(record, "ADDR", addr + "," + cty)

    elif ty == "2":
        if len(au) > 2:
            ckr.save2json(record, "AU", au)
        pass
    elif ty == "3":
        ckr.save2json(record, "AGC", au)


if __name__ == "__main__":
    record = {}
    AN = ""
    an = ""

    for line in sys.stdin:
        line = line.strip();
        items = line.split("\t")

        if len(items) == 6:
            an, ty, no, au, cty, addr = items[0], items[1], items[2], items[3], items[4], items[5]

            if AN == "":
                AN = an
                saveline(ty, au, cty, addr)

            elif AN == an:
                saveline(ty, au, cty, addr)

            elif AN != an:
                record["AN"] = AN
                print json.dumps(record, ensure_ascii=False)

                AN = an
                record = {}
                saveline(ty, au, cty, addr)


    record["AN"] = an
    print json.dumps(record, ensure_ascii=False)

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    ti_en = ""
    ti_fr = ""
    ti = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            field = field.strip()
            value = value.strip()

            # 取英文
            if field == "TI.EN":
                ti_en = value
            # 取法文
            if field == "TI.FR":
                ti_fr = value

            if not (field == "PN" or field == "TI.EN" or field == "TI.FR"):
                print line

            # 遇到PN，本单元结束
            if field == "PN":
                if ti_en != "":
                     ti = ti_en
                else:
                     ti = ti_fr
               
                if ti != "":
                    print "TI" + "\t" + ti
                print line

                ti_en = ""
                ti_fr = ""
                ti = ""

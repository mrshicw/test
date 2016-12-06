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
        if len(items) == 3:
            key, field, value = items[0], items[1], items[2]
            field = field.strip()
            value = value.strip()

            # 取英文
            if field == "TI.EN":
                ti_en = line
            # 取韩文
            if field == "TI.KR":
                ti_fr = line

            if not (field == "AN" or field == "TI.EN" or field == "TI.KR" or field == "TI.SUB"):
                print line

            # 遇到PN，本单元结束
            if field == "AN":
                if ti_en != "":
                     ti = ti_en
                else:
                     ti = ti_fr
               
                if ti != "":
                    ti = ti.replace("TI.EN", "TI")
                    ti = ti.replace("TI.KR", "TI")
                    tmp = ti.split("\t")
                    if len(tmp[2]) > 2:
                        print ti
                print line

                ti_en = ""
                ti_fr = ""
                ti = ""
        else:
            print line

###########################################################33333

    if ti_en != "":
        ti = ti_en
    else:
        ti = ti_fr
    if ti != "":
        ti = ti.replace("TI.EN", "TI")
        ti = ti.replace("TI.KR", "TI")
        tmp = ti.split("\t")
        if len(tmp[2]) > 2:
            print ti

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    pn = ""
    PN = ""
    ab_en = ""
    ab_fr = ""
    ab = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            field = field.strip()
            value = value.strip()

            # 取英文
            if field == "AB.EN":
                ab_en = value
            # 取法文
            if field == "AB.FR":
                ab_fr = value

            if not(field == "PN" or field == "AB.EN" or field == "AB.FR"):
                print line

            # 遇到PN，本单元结束
            if field == "PN":
                if ab_en != "":
                     ab = ab_en
                else:
                     ab = ab_fr
               
                if ab != "":
                    print "AB" + "\t" + ab
                print line

                ab_en = ""
                ab_fr = ""
                ab = ""

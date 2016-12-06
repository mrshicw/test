#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re


def save_dict(field, value):
    if field == "":
        field = value
    else:
        field = field + ";" + value

    return field


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        key, field = items[0], items[1]
        if field.startswith("(30) Priority info. (Country / No. / Date)"):
            value = field.replace("(30) Priority info. (Country / No. / Date)", "")

            pr = ""
            prc = ""
            prn = ""
            prd = ""
            PR = ""
            PRC = ""
            PRN = ""
            PRD = ""
            values = value.split("(")
            for value in values:
                value = value.replace(")", "")
                value = value.replace("   ", " ")
                value = value.replace("  ", " ")
                value = value.replace(" | ", "|")
                value = value.replace(" |", "|")
                value = value.replace("| ", "|")
                terms = value.split("|")
                if len(terms) == 3:
                    prc, prn, prd = terms[0], terms[1], terms[2]
                    prn =  re.sub(r'(\(.+?\))', "", prn)
                    prd = prd.replace(".", "")
                    prd = prd[0 : 8]

                    pr = prc + " " + prn + " " + prd
                    PR = save_dict(PR, pr)
                    PRC = save_dict(PRC, prc)
                    PRN = save_dict(PRN, prn)
                    PRD = save_dict(PRD, prd)

            if PR != "":
                print key + "\t" + "PR" + "\t" + PR
                print key + "\t" + "PRC" + "\t" + PRC
                print key + "\t" + "PRN" + "\t" + PRN
                print key + "\t" + "PRD" + "\t" + PRD
        else:
            print line

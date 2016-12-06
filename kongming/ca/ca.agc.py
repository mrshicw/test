#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re

def del_brace(line):
    line = line.replace("(KEAY) ", "")
    line = line.replace("(PHIL) ", "")
    line = line.replace("(BILL) ", "")
    line = line.replace("(BRUCE) ", "")
    line = line.replace("(WEI LI) ", "")
    line = line.replace("(JASON) ", "")
    line = line.replace("(THOMAS) ", "")
    line = line.replace("(Country Unknown)T(Country Unknown) ", "")
    line = line.replace("X(Country Unknown) ", "")
    line = line.replace("X(Not Available) ", "")
    line = line.replace("(KUANG)) ", "")
    line = line.replace("(JASON ) ", "")

    line = line.replace(" (KEAY)", "")
    line = line.replace(" (PHIL)", "")
    line = line.replace(" (BILL)", "")
    line = line.replace(" (BRUCE)", "")
    line = line.replace(" (WEI LI)", "")
    line = line.replace(" (JASON)", "")
    line = line.replace(" (THOMAS)", "")
    line = line.replace(" (Country Unknown)T(Country Unknown)", "")
    line = line.replace(" X(Country Unknown)", "")
    line = line.replace(" X(Not Available)", "")
    line = line.replace(" (KUANG)", "")
    line = line.replace(" (JASON )", "")

    line = line.replace("(KEAY)", "")
    line = line.replace("(BILL)", "")
    line = line.replace("(BRUCE)", "")
    line = line.replace("(WEI LI)", "")
    line = line.replace("(JASON)", "")
    line = line.replace("(THOMAS)", "")
    line = line.replace("(Country Unknown)T(Country Unknown)", "")
    line = line.replace("X(Country Unknown)", "")
    line = line.replace("X(Not Available)", "")
    line = line.replace("(KUANG)", "")
    line = line.replace("(JASON )", "")

    line = line.replace("(Iran (Islamic Republic of))", ";")
    line = line.replace("(Germany (Democratic Republic))", ";")
    line = line.replace("(Virgin Islands (British))", ";")
    line =  re.sub(r'(\(.+?\))', ";", line)
    items = line.split(";")
    line = ""
    for word in items:
        if not( word == "" or word == " "):
            if line == "":
               line = word
            else:
               line = line + ";" + word
    line = line.replace("; ", ";")
    line = line.replace(" ;", ";")
    return line


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            value = value.strip()
            if field == "AGC":
                value = del_brace(value)
                if not (value == "NA" or value.startswith("NA ")):
                    print "AGC" + "\t" + value
            else:
                print line

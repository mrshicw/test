#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re

def ipcr(term):
    m = re.search(r"([a-zA-Z]+)\s*(\d+)\s*([a-zA-Z]+)\s*0*([1-9][0-9]*)(/\d+)", term)

    if m != None:
        return "\x01".join(m.groups());

    else:
        m = re.search(r"([a-zA-Z]{1})([0-9]{2,3})([a-zA-Z]{1})([ 0-9]{3})(\d+)", term)
        if m != None:
            sec = m.group(1);
            cls = m.group(2);
            subcls = m.group(3);
            grp = str( int(m.group(4) ));
            subgrp = str( int(m.group(5)))

            return sec + "\x01" + cls + "\x01" + subcls + "\x01" + grp + "\x01/" + subgrp

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

def val_save(value, item):
    if value == "":
        value = item
    else:
        value = value + ";" + item
    return value

def ipcr_fmt(value):
    value = del_brace(value)
    items = value.split(";")
    value = ""
    for item in items:
        item = ipcr(item)
        if item != None:
            value = val_save(value, item)
    if value != "":
        return str(value)

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            if field == "IPCR":
                if value != "N/A":
                    value = ipcr_fmt(value)
                    print "IPCR" + "\t" + value
            else:
                print line

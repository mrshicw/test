#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        key, field = items[0], items[1]
        if field.startswith("(87) Int'l Unex. Pub. No.(Date)"):
            value = field.replace("(87) Int'l Unex. Pub. No.(Date)", "")

            ipnn = ""
            ipnd = ""
            value = value.replace(")", "")
            values = value.split("(")
            if len(values) == 2:
                ipnn = values[0].replace(" ", "")
                ipnd = values[1].replace(".", "")

            if ipnn != "":
                print key + "\t" + "IPN" + "\t" + "NONE" + " " + ipnn + " " + ipnd
                print key + "\t" + "IPNN" + "\t" + ipnn
                print key + "\t" + "IPND" + "\t" + ipnd
        else:
            print line

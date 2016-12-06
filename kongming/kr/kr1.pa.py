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
        if field.startswith("(71) Applicant"):
            value = field.replace("(71) Applicant", "")
            print key + "\t" + "PA" + "\t" + value
        else:
            print line

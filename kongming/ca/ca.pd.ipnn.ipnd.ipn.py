#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    pn = ""
    PN = ""
    pd = ""
    ipnn = ""
    ipnd = ""
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            field, value = items[0], items[1]
            value = value.strip()

            if field == "PD":
                pd = value
            if field == "IPNN":
                ipnn = value
            if field == "IPND":
                ipnd = value

            if not (field == "PN" or field == "PD" or field == "IPNN" or field == "IPND"):
                print line

            # 遇到PN，本单元结束
            if field == "PN" :
                pd = pd.replace("-", "")
                ipnn = ipnn.replace(" ", "")
                ipnd = ipnd.replace("-", "")

                if pd == "":
                    pd = ipnd
                if pd != "":
                    print "PD" + "\t" + pd

                if ipnn != "":
                    if ipnd == "":
                        ipnd = pd
                    print "IPNN" + "\t" + ipnn
                    print "IPND" + "\t" + ipnd
                    print "IPN" + "\t" + "NONE" + " " + ipnn + " " + ipnd
                print line

                pd = ""
                ipnn = ""
                ipnd = ""


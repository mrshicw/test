#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

def fmtpn_u65(pn):
    if pn.startswith("10"):
        pn = pn + "A"
    elif pn.startswith("20"):
        pn = pn + "U"
    return pn

def fmtpn_p11(pn):
    if pn.startswith("10"):
        pn = pn + "B1"
    elif pn.startswith("20"):
        pn = pn + "Y1"
    return pn

def getpnpd(value):
    items = value.split("(")
    pn = ""
    pd = ""
    if len(items) == 1:
        pd = items[-1]
    if len(items) == 2:
        pn = str(items[0])
        pd = items[1]

    pn = pn.replace(" ", "")
    pd = pd.replace(".", "")
    pd = pd.replace(")", "")

    return pn, pd

if __name__ == "__main__":
    AN = ""
    an = ""
    p11 = ""
    r11 = ""
    u65 = ""

    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        if len(items) == 2:
            key, value = items[0], items[1]
            an = key
            if AN == "":
                AN = an

            if AN != an:
                pnpds = u65 + "|" + p11 + "|" + r11
                tmps = pnpds.split("|")

                if tmps[2] == "" and len(tmps) == 6:
                    tmps[2] = tmps[4]
                if tmps[0] != "":
                    tmps[0] = "KR" + fmtpn_u65(tmps[0])
                if tmps[2] != "":
                    tmps[2] = "KR" + fmtpn_p11(tmps[2])
                if not (tmps[0] == "" and tmps[2] == ""):
                    pnpds = tmps[0] + "|" + tmps[1] + "|" + tmps[2] + "|" + tmps[3]
                    print AN + "\t" + pnpds

                AN = an
                u65 = ""
                p11 = ""
                r11 = ""

            if value.startswith("(11) Publication No.(Date)"):
                p11 = value.replace("(11) Publication No.(Date)", "")
                pn, pd = getpnpd(p11)
                p11 = pn + "|" + pd
            elif value.startswith("(11) Registration No.(Date)"):
                r11 = value.replace("(11) Registration No.(Date)", "")
                pn, pd = getpnpd(r11)
                r11 = pn + "|" + pd
            elif value.startswith("(65) Unex. Pub. No.(Date)"):
                u65 = value.replace("(65) Unex. Pub. No.(Date)", "")
                pn, pd = getpnpd(u65)
                u65 = pn + "|" + pd

    pnpds = u65 + "|" + p11 + "|" + r11
    tmps = pnpds.split("|")

    if tmps[2] == "":
        tmps[2] = tmps[4]
    if tmps[0] != "":
        tmps[0] = "KR" + fmtpn_u65(tmps[0])
    if tmps[2] != "":
        tmps[2] = "KR" + fmtpn_p11(tmps[2])

    if not (tmps[0] == "" and tmps[2] == ""):
        pnpds = tmps[0] + "|" + tmps[1] + "|" + tmps[2] + "|" + tmps[3]
        print AN + "\t" + pnpds

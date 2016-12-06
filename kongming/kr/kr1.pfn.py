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
        if field.startswith("Family No.") or field.startswith("Related Application No."):
            value = field.replace("Family No.", "")
            value = field.replace("Related Application No.", "")
            
            value = value.replace("&nbsp", "")
            val_len = len(value)
            list = []
            if val_len > 6:
                n = val_len / 13
                for i in range(0, n):
                    list.append("KR" + value[i * 13 : (i + 1) * 13])
                value = ";".join(list)

            print key + "\t" + "PFN" + "\t" + value
        else:
            print line

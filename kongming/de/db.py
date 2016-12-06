#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)

def run(line):
    line = line.strip();
    items = line.split("\t")

    if len(items) == 3:
        key, field, value = items[0], items[1], items[2]
        obj = ("AN", "PN", "LE", "LSN", "PR", "PFN", "CTN",  "CDN", "IPN", "IAN", "CTD", "QWFT", "CLM")
        if field in obj:
            return key + "\t" + field + "\t" + value + "\t0\t2"
        else:
            return key + "\t" + field + "\t" + value
        
if __name__ == "__main__":
    for line in sys.stdin:
        line = run(line)
        print line

        
        

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import json



def outrecord(record):
    an = record["AN"]
    for key in record:
        if key != "AN":
            if key == "ADDR":
                items = record[key].split(";")
                record[key] = items[0]
            print record["AN"] + "\t" + key + "\t" + record[key]

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        record = json.loads(line)
        outrecord(record)

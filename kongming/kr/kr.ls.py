#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split(">")

        if len(items) == 2:
            line = items[1]
            line = line.strip()
            print line

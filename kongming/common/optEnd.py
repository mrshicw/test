#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
if __name__ == "__main__":
    endchar = sys.argv[1]

    for line in sys.stdin:
        line = line.strip()
        if line.endswith(endchar) :
            print line

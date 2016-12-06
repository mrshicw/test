#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    print "#bin"
    for line in sys.stdin:
        line = line.strip()
        print "echo \"" + line + "\" | ./ca.raw.sh >> ca.raw.1104"

#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip();
        if line.startswith("Url:http://www"):
            print "\n" + line,
        elif line.startswith("LOG_WARNING"):
            pass
        else:
            print "|||" + line,

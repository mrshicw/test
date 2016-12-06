#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)

if __name__ == "__main__":
    dir = "ca"
    dir = sys.argv[1]
    cod = sys.argv[2]

    N = 0
    n = 10000
    num = 0
    print "#bin"
    for line in sys.stdin:
        line = line.strip()
        items = line.split("/")
        file = items[-1]

        N = N + 1
        if N % n == 1:
            num = num + 1
            print "mkdir -p " + str(dir) + "/" + str(num)
        f = line
        t = str(dir) + "/" + str(num) + "/" + file
        print "iconv -f " + cod + " -t utf-8 < " + f + " > " + t

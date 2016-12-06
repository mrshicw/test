#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    dict = {}
    for line in sys.stdin:
        line = line.strip()

        items = line.split("/")
        file = items[-1]
        dir = line

        if file not in dict:
            dict[file] = dir
        elif len(dict[file]) < len(dir):
            dict[file] = dir
        elif dict[file] < dir:
            dict[file] = dir


    print "#bin"
    for key in dict:
        files = key.split(".")
        an = files[0]
        length = len(an)

        if length <= 3:
            dir = "0000"
        elif length > 3 and length <= 6:
            dir = str(an[0 : 3])
        elif length > 6 and length <= 9:
            dir = str(an[0 : 3]) + "/" + str(an[3 : 6])
        elif length > 9 and length <= 12:
            dir = str(an[0 : 3]) + "/" + str(an[3 : 6]) + "/" + str(an[6 : 9])
        elif length > 12 and length <= 15:
            dir = str(an[0 : 3]) + "/" + str(an[3 : 6]) + "/" + str(an[6 : 9]) + "/" + str(an[9 : 12])
        elif length > 15 and length <= 18 :
            dir = str(an[0 : 3]) + "/" + str(an[3 : 6]) + "/" + str(an[6 : 9]) + "/" + str(an[9 : 12]) + "/" + str(an[12 : 15])

        html_dir = "/data/d0/data_html/ca/" + dir
        html_from = dict[key]
        html_to = html_dir + "/" + key

        print "mkdir -p " + html_dir
        print "iconv -f iso88591 -t utf-8 < " + html_from + " > " + html_to

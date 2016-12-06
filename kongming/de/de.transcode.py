#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    dict = {}
    for line in sys.stdin:
        line = line.strip()

        if ".2" in line:
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

        if length <= 5:
            dir = "0000"
        elif length > 5 and length <= 8:
            dir = str(an[2 : 5])
        elif length > 8 and length <= 11:
            dir = str(an[2 : 5]) + "/" + str(an[5 : 8])
        elif length > 11 and length <= 14:
            dir = str(an[2 : 5]) + "/" + str(an[5 : 8]) + "/" + str(an[8 : 11])
        elif length > 14 and length <= 17:
            dir = str(an[2 : 5]) + "/" + str(an[5 : 8]) + "/" + str(an[8 : 11]) + "/" + str(an[11 : 14])
        elif length > 17 and length <= 20:
            dir = str(an[2 : 5]) + "/" + str(an[5 : 8]) + "/" + str(an[8 : 11]) + "/" + str(an[11 : 14]) + "/" + str(an[14 : 17])

        html_dir = "/data/d0/data_html/de/" + dir
        html_from = dict[key]
        html_to = html_dir + "/" + key

        print "mkdir -p " + html_dir
        print "iconv -f iso88591 -t utf-8 < " + html_from + " > " + html_to

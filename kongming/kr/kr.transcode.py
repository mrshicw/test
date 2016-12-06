#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

if __name__ == "__main__":
    dict = {}
    for line in sys.stdin:
        line = line.strip()

        if ".pdf" in line:
            pass
        else:
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

        if length <= 4:
            dir = str(an)
        elif length > 4 and length <= 8:
            dir = str(an[0 : 4]) + "/" + str(an[4 : length])
        elif length > 8 and length <= 11:
            dir = str(an[0 : 4]) + "/" + str(an[4 : 8]) + "/" + str(an[8 : length])
        else:
            dir = str(an[0 : 4]) + "/" + str(an[4 : 8]) + "/" + str(an[8 : 11]) + "/" + str(an[11 : length])

        html_dir = "/data/d0/data_html/kr/" + dir
        html_from = dict[key]
        html_to = html_dir + "/" + key

        print "mkdir -p " + html_dir
        print "iconv -f utf-8 -t utf-8 < " + html_from + " > " + html_to

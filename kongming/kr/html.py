#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import HTMLParser

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        line = line.replace("&nbsp;", " ")
        html_parser = HTMLParser.HTMLParser()
        line = html_parser.unescape(line)
        print line

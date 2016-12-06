#!/usr/bin/env python
#!coding: utf8

import sys
import re
import lxml.html

def get_xpath(node, xpath, xpath_dict):
    children = node.getchildren();
    if len(children) == 0:
        if "/".join(xpath) not in xpath_dict:
            xpath_dict[ "/".join(xpath) ] = 0;
        xpath_dict[ "/".join(xpath) ] += 1;
    for child in children:
        xpath.append(child.tag);
        get_xpath(child, xpath, xpath_dict);
        xpath.pop();


if __name__ == "__main__":
    text = sys.stdin.read();

    #print text

    root = lxml.html.fromstring(text);
    xpath = [];
    xpath_dict = {}
    get_xpath(root, xpath, xpath_dict);
    for x in xpath_dict:
        print x + "\t" + str(xpath_dict[x])



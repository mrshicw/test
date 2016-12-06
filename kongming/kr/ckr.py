#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import re
import json
dict = {}
def load():
    f = open("kr.dict")
    for line in f.readlines():
        items = line.strip().split("\t")
        dict[items[0]] = items[1]
    f.close()
    return dict

def outrecord(record):
    if len(record) !=  0:
        for key in record:
            print record["PN"] + "\t" + key + "\t" + record[key]
def join2(key, value):
    return key + "\t" + value

def join3(key, field, value):
    return key + "\t" + join2(field, value)

def joins(key, field, value):
    return join3(key, field, value)


def load_pn_pd(filename):
    dictpn = {}
    dictpd = {}
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        items = line.split("\t")
        if len(items) == 3:
            an, pn, pd = items[0], items[1], items[2]
            dictpn[an] = pn
            dictpd[an] = pd
    f.close()

    return dictpn, dictpd


def init(rec, n):
    for i in range(0, n + 1):
        N = str(i)
        rec[N] = ""

def getpn(line):
    pn = ""
    items = line.strip().split("\t")
    tmp = items[0].split("/")
    f = tmp[len(tmp) - 1]
    files = f.split(".")
    an = files[0]

    if an in dict:
        pn = dict[an]
    else:
        pn = an

    return pn

def save2json(record, key, value):
    if key in record:
        record[key] = record[key] + ";" + value
    else:
        record[key] = value

def save(value, item):
    if value == "":
        value = item
    else:
        value = value + ";" + item
    return value

def del_brace(value):
    value =  re.sub(r'(\(.+?\))', ";", value)
    return value



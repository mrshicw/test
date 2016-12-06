#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
import re
def ipc(term):
    m = re.search(r"([a-zA-Z]+)\s*(\d+)\s*([a-zA-Z]+)\s*0*([1-9][0-9]*)(/\d+)", term);
    if m != None:
        return "\x01".join(m.groups());

    else:
        m = re.search(r"([a-zA-Z]{1})([0-9]{2,3})([a-zA-Z]{1})([ 0-9]{3})(\d+)", term);
        if m != None:
            sec = m.group(1);
            cls = m.group(2);
            subcls = m.group(3);
            grp = str( int(m.group(4) ));
            subgrp = str( int(m.group(5)))
            return sec + "\x01" + cls + "\x01" + subcls + "\x01" + grp + "\x01/" + subgrp

def ipc_format(value):
    list = []
    items = value.split(";")
    for item in items:
        item = item.strip()
        item = ipc(item)
        if item != None:
            list.append(item)
    value = ";".join(list)

    return value

def run(line):
    line = line.strip();
    items = line.split("\t")

    if len(items) == 2:
        field, value = items[0], items[1]
        if field == "IPC":
            value = ipc_format(value)
            print "IPC" + "\t" + value
        else:
            print line
    elif len(items) == 3:
        key, field, value = items[0], items[1], items[2]
        if field == "IPC":
            value = ipc_format(value)
            print key + "\t" + "IPC" + "\t" + value
        else:
            print line
    else:
        print line
        
if __name__ == "__main__":
    for line in sys.stdin:
        run(line)

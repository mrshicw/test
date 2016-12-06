#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")
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

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        items = line.split("\t")
        key, field = items[0], items[1]
        if field.startswith("(51) Int. CL"):
            value = field.replace("(51) Int. CL", "")

            if value != "":
                value = re.sub(r'(\(.+?\))', ";", value)
                items = value.split("\t")
                value = ""
                for item in items:
                    if value == "":
                        value = item
                    else:
                        value = value + ";" + item


            list = []
            items = value.split(";")
            for item in items:
                item = ipc(item)
                if item != None:
                    list.append(item)
            value = ";".join(list)
            if value != "":
                print key + "\t" + "IPC" + "\t" + value

        else:
            print line

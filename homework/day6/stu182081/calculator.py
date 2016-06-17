#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
def jiajian(val):
    key = re.search('\d+\.*\d*[\+\-]+[\+\-]?\d+\.*\d*', val)
    if  key:
        content = key.group()
        if len(content.split('+')) > 1:
            value = float(content.split('+')[0]) + float(content.split('+')[1])
        else:
            value = float(content.split('-')[0]) - float(content.split('-')[1])
        before, after = re.split('\d+\.*\d*[\+\-]+[\+\-]?\d+\.*\d*', val, 1)
        val = "%s%s%s" % (before, value, after)
        return val
def new(val):
    while( '*'  in val) or ('/') in val:
        val =chengchu(val)
    return val
def chengchu(val):
    key = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val)
    if  key:
        content = key.group()
        if len(content.split('*')) > 1:
            value = float(content.split('*')[0]) * float(content.split('*')[1])
        else:
            value = float(content.split('/')[0]) / float(content.split('/')[1])
        before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val, 1)
        val = "%s%s%s" % (before, value, after)
        return val
def new_2(val):
    while ('+' in val) or ('-' in val):
        val = jiajian(val)
    return val
origin = "12/3+3*(4+5)/8-6+6+8*8+(6*7*9)+(4*6)+5"
while True:
    result = re.split("\(([^()]+)\)", origin, 1)
    if len(result) == 3:
        before, content, after = result
        r = new_2(new(content))
        new_str = before + str(r) + after
        origin = new_str
    else:
        final = new_2(new(origin))
        print(final)
        break
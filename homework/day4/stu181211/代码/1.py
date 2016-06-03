#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
寻找差异
# 数据库中原有
old_dict = {
    "#1":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 80 }
    "#3":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 80 }
}

# cmdb 新汇报的数据
new_dict = {
    "#1":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 80 }
    "#4":{ 'hostname':c2, 'cpu_count': 2, 'mem_capicity': 80 }
}
"""

#定义旧字典变量
old_dict = {
    "#1": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80},
    "#2": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80},
    "#3": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80}
}

#定义新字典变量
new_dict = {
    "#1": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 800},
    "#3": {'hostname': "c2", 'cpu_count': 2, 'mem_capicity': 80},
    "#4": {'hostname': "c2", 'cpu_count': 2, 'mem_capicity': 80}
}

#对两个字典的键值进行比较
#1 如果一个健值在新字典中有，在旧字典中没有，则在旧字典中添加
#2 如果一个健值在新旧字典中都有，但是值不同，则将新的值更新入旧字典
#3 如果一个健值只在旧的字典中有，在新字典中没有，则删除旧字典中该健值
#最后打印出修改后的旧字典

oldkeys = old_dict.keys()
newkeys = new_dict.keys()

#处理只有新字典有，旧字典没有的key，添加入旧字典
for key in set(newkeys).difference(set(oldkeys)):
    old_dict[key] = new_dict[key]

#处理只有旧字典有，新字典没有的key，从旧字典中删除
for key in set(oldkeys).difference(set(newkeys)):
    old_dict.pop(key)

#处理新字典和旧字典中都有的key，将新值更新入旧字典
for key in set(newkeys).intersection(set(oldkeys)):
    if new_dict[key] != old_dict[key]:
        old_dict[key] = new_dict[key]

#打印出最后更新完成的旧字典
import pprint
print("更新后的旧字典：")
pprint.pprint(old_dict)
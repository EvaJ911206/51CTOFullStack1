#!/usr/bin/env python
# coding:utf-8
# 寻找两个字典的差异
"""
需要删除：？
需要新建：？
需要更新：？
注意：无需考虑内部元素是否改变，只要原来存在，新汇报也存在，就是需要更新
"""
# 数据库中原有
old_dict = {
    "#1": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80},
    "#2": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80},
    "#3": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80}
}

# cmdb 新汇报的数据
new_dict = {
    "#1": {'hostname':"c1", 'cpu_count': 2, 'mem_capicity': 800},
    "#3": {'hostname':"c1", 'cpu_count': 2, 'mem_capicity': 80},
    "#4": {'hostname':"c2", 'cpu_count': 2, 'mem_capicity': 80}
}
del_dict = {}
built_dict = {}
update_dict = {}

old_set = set(old_dict)
new_set = set(new_dict)
# 需要删除：
del_set = old_set.difference(new_set)
for item in del_set:
    del_dict[item] = old_dict[item]
print(del_dict)
# 需要新建：
built_set = new_set.difference(old_set)
for item in built_set:
    built_dict[item] = new_dict[item]
print(built_dict)
# 需要更新：
update_set = old_set.intersection(new_set)
for item in update_set:
    update_dict[item] = new_dict[item]
print(update_dict)
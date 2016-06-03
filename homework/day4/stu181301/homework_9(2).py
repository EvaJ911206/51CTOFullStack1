#!/usr/bin/env python
# -*- coding:utf-8 -*-
old_dict = {
    "#1": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80},
    "#2": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80},
    "#3": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80}
}
# cmdb 新汇报的数据
new_dict = {
    "#1": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 800},
    "#3": {'hostname': "c1", 'cpu_count': 2, 'mem_capicity': 80},
    "#4": {'hostname': "c2", 'cpu_count': 2, 'mem_capicity': 80}
}
# 找出需要删除：
# 找出需要新建：
# 找出需要更新：
# 注意：无需考虑内部元素是否改变，只要原来存在，新汇报也存在，就是需要更新

old_key = old_dict.keys() #['#3', '#2', '#1']
new_key = new_dict.keys() #['#3', '#1', '#4']

old_set = set(old_key)
new_set = set(new_key)


del_set = old_set.difference(new_dict) #查找两个集合的差集，得到删除的集合
print("需删除的元素: %s" %del_set) #[2]

add_set = new_set.difference(old_set) #查找两个集合的差集，得到新增的集合
print("需要更新的元素: %s" %add_set) #[4]

update_set = old_set.intersection(new_set) #查找两个集合的交集，得到新建的集合
print("需要新建的集合: %s" %update_set) #['#3', '#1']
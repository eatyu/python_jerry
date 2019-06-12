#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# set
print('\n11.set')
set1 = set([123, 456, 789])
print(set1)

# 经过之前的学习，可以知道，tuple (元组) 使用小括号，
# list (列表) 使用方括号, dict (字典) 使用的是大括号，
# dict 也是无序的，只不过 dict 保存的是 key-value 键值对值，
# 而 set 可以理解为只保存 key 值。
#
set1.add(100)
print(set1)
set1.remove(456)
print(set1)

#
#
#
#

set3 = ['hello']
set1 = set('hello')
set2 = set(['p', 'y', 'y', 'h', 'o', 'n'])
print('\n')
print(set1)
print(set2)
print(set3)

# 交集 (求两个 set 集合中相同的元素)
set3 = set1 & set2
print('\n交集 set3:')
print(set3)
# 并集 （合并两个 set 集合的元素并去除重复的值）
set4 = set1 | set2
print('\n并集 set4:')
print(set4)
# 差集
set5 = set1 - set2
set6 = set2 - set1
print('\n差集 set5:')
print(set5)
print('\n差集 set6:')
print(set6)

# 去除海量列表里重复元素，用 hash 来解决也行，只不过感觉在性能上不是很高，用 set 解决还是很不错的
list1 = [111, 222, 333, 444, 111, 222, 333, 444, 555, 666]
set7 = set(list1)
print('\n去除列表里重复元素 set7:')
print(set7)

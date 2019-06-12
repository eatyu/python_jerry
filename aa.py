#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("sss")
#  不需要转义
a = r'不需要转义dasda/dsad/w/ads/wd/a\n'
print(a)
# 多行字符串
b = r'''多行
dasda
aaaa'''
print(b)
# 布尔类型
c = True
print(c)
# 空值
d = None
print(d)
# 整型，python3没有Long，只有int
e = 123456789012345678901234567890
print(e)
# 反复复制
f = 'abc'
print(f)
f = 123456789
print(f)
f = None
print(f)
f = True
print(f)
# 多个变量赋值
g = h = i = j = k = 100
print(g)

l = 909
m = str(l)
print(m)

list1 = ['两点水', 'twowter', 'liangdianshui', 123]
print(list1)
# 通过索引对列表的数据项进行修改或更新
list1[2] = 456
print(list1)
# 使用 append() 方法来添加列表项
list1.append('hello')
print(list1)
# 使用 del 语句来删除列表的的元素
del list1[1]
print(list1)

print(len([1, 2, 3]))  # 3	计算元素个数

print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]	组合
print(['Hi!'] * 4)  # ['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制
print(3 in [1, 2, 3])  # True	元素是否存在于列表中

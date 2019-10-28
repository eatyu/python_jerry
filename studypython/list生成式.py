#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 首先，lsit 生成式的语法为：
#
# [expr for iter_var in iterable]
# [expr for iter_var in iterable if cond_expr]

# range(x,y) 左开右闭
list1 = [x for x in range(1, 31)]
print(list1)

list2 = [x for x in range(1, 31) if x % 2 == 0]
print(list2)

list3 = [(x + 1, y + 1) for x in range(3) for y in range(5)]
print(list3)

list4 = [(x + 1, y + 1) for x in range(3) for y in range(5) if x == 2]
print(list4)

for i in range(4):
    print(i)
print("####")
L = [1, 3, 3, 1, 0]

oo = L[0 - 1] + L[0]
print(L[0 - 1])
print(L[0])
print(oo)

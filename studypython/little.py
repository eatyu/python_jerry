#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表
import functools

strv = 'abc'
strv2 = strv * 3
print(strv2)

lista = ['tom', 'ABC', 12]
listb = lista * 4
print(listb)

print('tom' in listb)
for x in lista:
    print(x)

listc = [1, 2, 3, 4, 5]
print(max(listc))
print(listc.count(2))
listc.extend(lista)
print(listc)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.sort(key=functools.cmp_to_key(lambda x, y: y - x))
print(numbers)

dict1 = {'liangdianshui': '111111', 123: '222222', (123, 'tom'): '333333', 'twowater': '444444'}

print(dict1[(123, 'tom')])

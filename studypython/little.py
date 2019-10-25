#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表

strv = 'abc'
strv2 = strv * 3
print(strv2)

lista = ['tom', 'ABC', 12]
listb = lista * 4
print(listb)

print('tom' in listb)
for x in lista:
    print(x)

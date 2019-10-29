#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def a():
    """函数：30以下整数数字列表生成器"""
    for i in range(30):
        yield i


num_gen = (i for i in range(30))

# 观察下面的输出 还蛮有趣的
print(type(a()))  # a()是个生成器
print(type(a))  # a 是函数
print(a())  # a() 是生成器
print(type(num_gen))

# for n in num_gen:
#     print(n, end=" ")

print()

# for a in a():
#     print(a, end=" ")

print(next(a()))

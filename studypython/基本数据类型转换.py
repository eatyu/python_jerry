#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = 12
str_v = '123'
# int(x [,base ])	将x转换为一个整数
# int('字符串',这里表示前面的字符串是多少进制的字符串)
print(int('1C', 16))
print(int('071', 8))
print(int(x))

# float(x )	将x转换到一个浮点
print(float(x))

# complex(real [,imag ])	创建一个复数
complexv = complex(12, 45)
print(complexv)
print(type(complexv))

# str(x )	将对象 x 转换为字符串
# repr(x )	将对象 x 转换为表达式字符串
print(str(complexv))
print(repr(complexv))

# eval(str )	用来计算在字符串中的有效 Python 表达式,并返回一个对象
# 这个方法好啊，可以实现简单的计算器
re = eval('1+3')
print(re)
print(id(re))

# tuple(s )	将序列 s 转换为一个元组
# list(s )	将序列 s 转换为一个列表
# chr(x )	将一个整数转换为一个字符
# unichr(x )	将一个整数转换为 Unicode 字符
# ord(x )	将一个字符转换为它的整数值
# hex(x )	将一个整数转换为一个十六进制字符串
# oct(x )	将一个整数转换为一个八进制字符串

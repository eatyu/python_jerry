#!/usr/bin/env python3
# -*- coding: utf-8 -*-


info = """万物之始-元"""


class Item:
    pass


# 打印类的类型，输出是‘type’
print(type(Item))

# 打印实例对象的类型，object
it1 = Item()
print(type(it1))


# 其实 type() 函数不仅可以返回一个对象的类型，也可以创建出新的类型。
# class 的定义是运行时动态创建的，而创建 class 的方法就是使用 type() 函数


# 定义一个函数，作为当来动态生成class时的一个方法
def info_fun(self):
    print(info)


def name_fun(self):
    print("我是动态生成的类")


ItemDy = type('ItemDy', (object,), dict(info=info_fun, name=name_fun))
ItemDy2 = type('ItemDy2', (object,), {'info': info_fun, 'name': name_fun})

dy1 = ItemDy()

dy1.info()
dy1.name()

dy2 = ItemDy2()
dy2.name()

print(type(dy1))
print(type(ItemDy))

# 输出的结果，可以看到，通过 type() 函数创建的类和直接写 class 是完全一样的。

# 这是因为Python 解释器遇到 class 定义时，仅仅是扫描一下 class 定义的语法，然后调用 type() 函数创建出 class 的。

print("查看生成它们这些东西的幕后是谁")
print(dy1.__class__)
print(ItemDy.__class__)

# 通过输出，得出生成对象的是定义的类，生成类的是个叫 type 的类

# 为了得到python一切类型的开始，把一些常用的类型生成并打印他们的创建者


num = 5  # 整型
ff = 5.01  # 浮点
isOk = True  # bool


def fun_1():
    pass


class Time(object):
    pass


print("查看常用类型生成者是谁")
print(num.__class__)
print(ff.__class__)
print(isOk.__class__)
print(fun_1.__class__)
print(Time.__class__)

# 得出常用类型是这些类生成的

print("查看生成 “能生成常用类型的类” 的类是谁")
print(num.__class__.__class__)
print(ff.__class__.__class__)
print(isOk.__class__.__class__)
print(fun_1.__class__.__class__)
print(Time.__class__.__class__)

# type 就是内建的元类。也就是 Python 自带的元类
# 元类是生成类的类

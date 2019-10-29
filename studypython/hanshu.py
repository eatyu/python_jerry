#!/usr/bin/env python3
# -*- coding: utf-8 -*-
_no_value = object()


def first_fun(a, b=_no_value):
    """函数_文档字符串，第一行可以放字符串，作为说明文本"""
    if b is _no_value:
        print("b没有传递")
    return


# first_fun(12,13)
first_fun(11)


def second_fun(v1, v2=None, v3=_no_value):
    """第二个函数"""
    print("{},{},{}".format(v1, v2, v3))


second_fun(1)

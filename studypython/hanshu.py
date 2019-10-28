#!/usr/bin/env python3
# -*- coding: utf-8 -*-
_no_value = object()


def firstfun(a, b=_no_value):
    """函数_文档字符串，第一行可以放字符串，作为说明文本"""
    if b is _no_value:
        print("b没有传递")
    return


# firstfun(12,13)
firstfun(11)

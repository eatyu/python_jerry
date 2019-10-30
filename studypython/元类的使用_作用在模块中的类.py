#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """返回一个类，将属性名转为大写"""
    # 取出类中的属性，过滤掉"__"开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    print("aaaaa")
    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = upper_attr


class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))


class Item(object):
    ae = "annie"


print(hasattr(Item, 'ae'))

#### 这个效果没有实现，暂时不知道原因

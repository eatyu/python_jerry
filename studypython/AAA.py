#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" review file
    edit during review
"""


def pass_fun(a=object()):
    """document string, the first line can put a string as explanatory text"""
    pass


# using lambda for simple calculation
sum = lambda e1, e2: e1 + e2

# list generator
list_a = [x for x in range(5)]

one = {'tom': 12, 'jerry': 11}
two = {'tom', 'jerry'}
print(type(one))
print(type(two))
print(two)
two.add("kk")
print(two)
two = set('tom')
print(two)


# Metaclass
def name(self):
    print("show metaclass")


def maxA(self, list):
    return max(list)


Meta = type("Meta", (object,), dict(name=name, max=maxA))

me = Meta()
me.name()
print(me.max(list_a))
print(maxA(None, list_a))

if type(list_a) is list:
    print("list_a is a list ")

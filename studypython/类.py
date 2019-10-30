#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Item(object):
    def __init__(self):
        print("万物之始，会归原初，不造一物，无形无相")


class Person(Item):
    name = ''

    def __init__(self):
        super().__init__()
        self.feature_list = ['衣', '食', '住', '行']

    def desp(self):
        print("人类")

    def set_name(self, name):
        self.name = name
        print("每个人都有命名权" + self.name)


class Sage(Item):
    """哲人 大智人"""
    pass


class FoolishMan(Person):
    """愚蠢的人"""

    def __init__(self):
        super().__init__()
        self.feature_list.append("愚蠢")
        self.feature_list.append("贪婪")
        self.feature_list.append("没有智慧")

    pass


def person_desp(self):
    print("人类是自私的，贪婪的，无知的，怠惰的，荒淫的")


p1 = Person()
p1.set_name("Jerry")
p1.desp()

# 替换类的方法
Person.desp = person_desp
# 方法替换后，在对象中也是生效的
p1.desp()

# 析构函数
del p1

p2 = FoolishMan()
print(p2.feature_list)

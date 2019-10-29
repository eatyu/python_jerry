#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Person(object):
    mz = ''

    def desp(self):
        print("info...")

    def name(self):
        self.mz = 'Tom'
        print("每个人都有命名权" + self.mz)


tom = Person()
tom.name()
tom.desp()


def aa(self):
    print("s")


Person.desp = aa

tom.desp()

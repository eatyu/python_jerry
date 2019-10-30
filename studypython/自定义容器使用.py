#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from studypython.自定义容器 import FunctionalList

mm = FunctionalList(["jerry", "cuku", "line"])

mm.append(1)
mm.append('a')
mm.append((1, 2))

print(mm)

for i in mm:
    print(i)

print(len(mm))

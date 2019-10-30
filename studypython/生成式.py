#!/usr/bin/env python3
# -*- coding: utf-8 -*-


list1 = [x * x for x in range(1, 31) if x % 2 == 0]
print(list1)

item_map = {"name": "Tom", "age": 14}

attr = ((name, value) for name, value in item_map)

print(attr)

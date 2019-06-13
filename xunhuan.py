#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 1
count = 0
while count < 100:
    a += 2
    count = count + 1
print(a)

b = 1
count = 0
while count < 100:
    b += 2
    count += 1
    if b > 100:
        break
print(b)

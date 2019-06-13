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

print("\n\n\n\n########")

for i in [1, 22, 3, 4, 500]:
    print(i)
else:
    print("cool you have read all words")

a = [1, 2, 3, 4, 5, 6, 7, 8]


def search(names, special):
    for name in names:
        if name == special:
            print("find")
            break
    else:
        print("not found")


firstname = ["tom", "tony", "zik"]
search(firstname, "tom")
search(firstname, "opop")

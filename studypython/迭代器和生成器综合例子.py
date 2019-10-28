#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Countdown:
    def __init__(self, start):
        self.start = start

    def __reversed__(self):
        # Reverse iterator
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __iter__(self):
        # Forward iterator
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print(rr)
print("######")
for rr in Countdown(30):
    print(rr)

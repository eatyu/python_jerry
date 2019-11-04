#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


def twoSum(in_array: List[int], target: int) -> List[int]:
    hashmap = {}
    for index, num in enumerate(in_array):
        if target - num in hashmap:
            return [hashmap[target - num], index]
        hashmap[num] = index
    return None


if __name__ == '__main__':
    in_array = [2, 2, 3, 4, 5]
    target = 5
    print(twoSum(in_array, target))

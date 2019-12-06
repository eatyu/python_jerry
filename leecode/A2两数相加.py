#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = None
        tail = None
        carry = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            val = num1 + num2 + carry
            carry = val // 10  # 取整
            current = val % 10
            cLN = ListNode(current)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if re is None:
                re = cLN
            if tail is None:
                tail = cLN
            else:
                tail.next = cLN
                tail = tail.next
        if carry > 0:
            tail.next = ListNode(carry)
        return re


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(7)
    l2.next.next = ListNode(5)
    solution = Solution()
    re = solution.addTwoNumbers(l1, l2)
    while re is not None:
        print(re.val)
        re = re.next

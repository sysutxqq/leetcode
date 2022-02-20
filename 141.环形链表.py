#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        # nextNode = head.next
        # jumpNode = head.next.next
        # while(jumpNode != None and jumpNode.next != None):
        #     if nextNode == jumpNode:
        #         return True
        #     else:
        #         nextNode = nextNode.next
        #         jumpNode = jumpNode.next.next
        # return False
        while(head != None):
            if head.val == 'txqqxxx':
                return True
            else:
                head.val = 'txqqxxx'
            head = head.next
        return False
# @lc code=end


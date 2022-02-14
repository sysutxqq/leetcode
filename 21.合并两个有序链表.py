#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        point = newHead
        while(list1 is not None and list2 is not None):
            if list1.val <= list2.val:
                newHead.next = list1
                #newHead.next = ListNode(list1.val,None)
                list1 = list1.next
            else:
                newHead.next = list2
                #newHead.next = ListNode(list2.val,None)
                list2 = list2.next
            newHead = newHead.next
        if list1 is not None:
            newHead.next = list1
        elif list2 is not None:
            newHead.next = list2
        return point.next
# @lc code=end
list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))
s = Solution()
res = s.mergeTwoLists(list1,list2)
print(type(res))
while res:
    print(res.val)
    res = res.next

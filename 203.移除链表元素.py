#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
from re import I


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        newHead = ListNode()
        curNode = newHead
        while(head.next != None):
            if head.val == val:
                head = head.next
            else:
                curNode.next = head
                curNode = curNode.next
            head = head.next
        return newHead.next
# @lc code=end
sol = Solution()
head = ListNode(1,ListNode(2,ListNode(6,ListNode(3,ListNode(4,ListNode(5,ListNode(6)))))))
res = sol.removeElements(head,6)

#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
from hashlib import new

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        curNode = head
        nextNode = curNode.next
        newHead = curNode
        while(nextNode != None):
            while nextNode != None and curNode.val == nextNode.val:
                nextNode = nextNode.next
            if nextNode == None:
                curNode.next = None
            else:
                curNode.next = nextNode
                nextNode = nextNode.next
                curNode = curNode.next
        return newHead
# @lc code=end
sol = Solution()
#head = ListNode(1,ListNode(1,ListNode(1,ListNode(1))))
head = ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3)))))
res = sol.deleteDuplicates(head)

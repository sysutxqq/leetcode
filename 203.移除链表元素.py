#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        newHead = ListNode()
        newHead.next = head
        curNode = newHead
        while(curNode.next):
            if curNode.next.val == val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return newHead.next
        # while(head):
        #     if head.val == val:
        #         if head.next:
        #             head = head.next
        #         else:
        #             head = head.next
        #             curNode.next = head
        #     else:
        #         curNode.next = head
        #         curNode = curNode.next
        #         head = head.next
        return newHead.next
# @lc code=end


#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # while(headA):
        #     curHeadB = headB
        #     while(curHeadB):
        #         if headA != curHeadB:
        #             curHeadB = curHeadB.next
        #         elif headA == curHeadB:
        #             return headA
        #     headA = headA.next
        # return None
        if headA == None or headB == None:
            return None
        curA = headA
        curB = headB
        while(curA != curB):
            if curA == None:
                curA = headB
            else:
                curA = curA.next
            if curB == None:
                curB = headA
            else:
                curB = curB.next
        return curB
# @lc code=end


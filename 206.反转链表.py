#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preList = None
        nextList = head
        while(nextList):
            tmp = nextList.next
            nextList.next = preList
            preList = nextList
            nextList = tmp
        return preList
# @lc code=end
sol = Solution()
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
res = sol.reverseList(head)


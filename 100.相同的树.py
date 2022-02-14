#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
            
        # inorderP = []
        # inorderQ = []
        # resP = []
        # resQ = []
        # while((p != None or q != None) or (len(inorderP) != 0 or len(inorderQ) != 0)):
        #     if p != None and q != None:
        #         inorderP.append(p)
        #         inorderQ.append(q)
        #         p = p.left
        #         q = q.left
        #     elif p == None and q == None:
        #         p = inorderP.pop()
        #         q = inorderQ.pop()
        #         if p.val != q.val:
        #             return False
        #         resP.append(p.val)
        #         resQ.append(q.val)
        #         p = p.right
        #         q = q.right
        #     else:
        #         return False
        # return True



    # def inorderTraversal(self,root: TreeNode)->List[int]:
    #     res = []
    #     if root is None:
    #         return res
    #     tmpStack = []
    #     currNode = root
    #     while(currNode != None or len(tmpStack) != 0):
    #         if currNode != None:
    #             tmpStack.append(currNode)
    #             currNode = currNode.left
    #         else:
    #             currNode = tmpStack.pop()
    #             res.append(currNode.val)
    #             currNode = currNode.right
    #     return res

# @lc code=end


#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        nodeStack = []
        curNode = root
        while(nodeStack or curNode):
            if curNode:
                nodeStack.append(curNode)
                res.append(curNode.val)
                curNode = curNode.left
            else:
                curNode = nodeStack.pop()
                curNode = curNode.right
        # self.preorderTraversalHelper(root,res)
        return res

    def preorderTraversalHelper(self,root:Optional[TreeNode],res:List[int]):
        if root == None:
            return
        res.append(root.val)
        self.preorderTraversalHelper(root.left,res)
        self.preorderTraversalHelper(root.right,res)
# @lc code=end


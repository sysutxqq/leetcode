#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        res = []
        self.hasPathSumHelper(root,res)
        if targetSum in res:
            return True
        return False
    
    def hasPathSumHelper(self,root:TreeNode,sums:List[int])->List[int]:
        if root == None:
            return 0
        leftNode = root.left
        if leftNode != None:
            leftSum = self.hasPathSumHelper(root.left,sums) + leftNode.val
            sums.append(leftSum)
        rightNode = root.right
        if rightNode != None:
            rightNode = self.hasPathSumHelper(root.right,sums) + rightNode.val
            sums.append(rightNode)
# @lc code=end


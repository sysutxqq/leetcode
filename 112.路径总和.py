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
        
        if root.val == targetSum:
            if root.left == None and root.right == None:
                return True
        leftRes = self.hasPathSum(root.left,targetSum - root.val)
        rightRes =  self.hasPathSum(root.right,targetSum - root.val)
        return leftRes or rightRes

# @lc code=end
root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2))),TreeNode(8,TreeNode(13),TreeNode(4,None,TreeNode(1))))
sol = Solution()
res = sol.hasPathSum(root,22)


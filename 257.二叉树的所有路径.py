#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
from pickle import LIST
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        res = []
        if root is None:
            return res
        subRes = ''
        self.binaryTreePathsHelper(root,subRes,res)
        return res

    def binaryTreePathsHelper(self,root:TreeNode,subRes:str,res:list[str]):
        subRes = subRes + str(root.val)
        if root.left is None and root.right is None: 
            res.append(subRes)
            return
        subRes = subRes + '->'
        if root.left:
            self.binaryTreePathsHelper(root.left,subRes,res)
        if root.right:
            self.binaryTreePathsHelper(root.right,subRes,res)
        
    
# @lc code=end

sol = Solution()
root = TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3))
res = sol.binaryTreePaths(root)
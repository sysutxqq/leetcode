#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        rootIndex = len(nums)//2
        root = TreeNode(nums[rootIndex])
        root.left = self.sortedArrayToBST(nums[:rootIndex])
        root.right = self.sortedArrayToBST(nums[rootIndex+1:])
        return root
        
# @lc code=end
sol = Solution()
nums = [-10,-3,0,5,9]
res = sol.sortedArrayToBST(nums)

#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        leftTreeHeight = self.isBalancedHelper(root.left)
        rightTreeHeight = self.isBalancedHelper(root.right)
        if abs(leftTreeHeight-rightTreeHeight) > 1:
            return False
        leftRes = self.isBalanced(root.left)
        rightRes = self.isBalanced(root.right)
        return leftRes and rightRes

    #求二叉树的最大深度
    def isBalancedHelper(self,root:TreeNode)->int:
        if root == None:
            return 0
        leftHeight = self.isBalancedHelper(root.left)
        rightHeight = self.isBalancedHelper(root.right)
        return max(leftHeight,rightHeight) + 1
# @lc code=end


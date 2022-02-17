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
        
        #中序遍历
        if root == None:
            return
        if root.val == targetSum:
            return True
        else:
            self.hasPathSum(root.left,targetSum - root.val)
            self.hasPathSum(root.right,targetSum - root.val)
        return False

        # if root == None:
        #     return False
        # res = []
        # self.hasPathSumHelper(root,res)
        # if targetSum in res:
        #     return True
        # return False
    
    def hasPathSumHelper(self,root:TreeNode,sums:List[int]):
        leftNode = root.left
        rightNode = root.right

        if root.left == None and root.right == None:
            return root.val
        leftSum = self.hasPathSumHelper(leftNode,sums) + root.val
        sums.append(leftSum)
        rightSum = self.hasPathSumHelper(rightNode,sums) + root.val
        sums.append(rightSum)
        print("nothing returned")

# @lc code=end
root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2))),TreeNode(8,TreeNode(13),TreeNode(4,None,TreeNode(1))))
sol = Solution()
res = sol.hasPathSum(root,22)


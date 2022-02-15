#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #1. 层序遍历
        # if root == None:
        #     return 0
        # else:
        #     nextLevelNode = [root]
        #     height = 0
        #     nextNodeNum = 1
        #     while(nextLevelNode):
        #         #遍历每一层
        #         while(nextNodeNum != 0):
        #             curNode = nextLevelNode.pop(0)
        #             if curNode.left == None and curNode.right == None:
        #                 nextNodeNum -= 1
        #                 break
        #             else:
        #                 if curNode.left != None:
        #                     nextLevelNode.append(curNode.left)
        #                 if curNode.right != None:
        #                     nextLevelNode.append(curNode.right)
        #             nextNodeNum -= 1
        #         if nextNodeNum == 0:
        #             height += 1
        #             nextNodeNum = len(nextLevelNode)
        #     return height
        #2. 递归
        if root == None:
            return 0 
        else:
            tmpNode = root.left
            leftLength = self.maxDepth(root.left)
            rightLength = self.maxDepth(root.right)
            return max(leftLength,rightLength) + 1
# @lc code=end
sol = Solution()
root = TreeNode(1,TreeNode(2,TreeNode(4),None),TreeNode(3,None,TreeNode(7)))
res = sol.maxDepth(root)


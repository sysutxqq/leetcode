#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tmpStack = []
        res = []
        currNode = root
        while(currNode != None or len(tmpStack) != 0):
            if currNode != None:
                tmpStack.append(currNode)
                currNode = currNode.left
            else:
                currNode = tmpStack.pop()
                res.append(currNode.val)
                currNode = currNode.right
        return res
    #     res = []
    #     if root == None:
    #         return res
    #     self.inorderTraversalHelper(root,res)
    #     return res

    
    # def inorderTraversalHelper(self,root:Optional[TreeNode],res:List[int]):
    #     if root == None:
    #         return 
    #     self.inorderTraversalHelper(root.left,res)
    #     res.append(root.val)
    #     self.inorderTraversalHelper(root.right,res)
        
# @lc code=end

root = TreeNode(1,None,TreeNode(2,TreeNode(3,None,None),None))
sol = Solution()
res = sol.inorderTraversal(root)
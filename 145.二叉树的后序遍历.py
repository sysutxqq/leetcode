#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        NodeStack = []
        curNode = root
        viewNode = None
        while(NodeStack or curNode):
            if curNode:
                NodeStack.append(curNode)
                curNode = curNode.left
            else:
                curNode = NodeStack[-1]
                if curNode.right == None or curNode.right == viewNode:
                    curNode = NodeStack.pop()
                    res.append(curNode.val)
                    viewNode = curNode
                    curNode = None
                else:
                    curNode = curNode.right

        # self.postorderTraversalHelper(root,res)
        return res
    
    def postorderTraversalHelper(self,root:TreeNode,res:List[int]):
        if root == None:  
            return
        self.postorderTraversalHelper(root.left,res)
        self.postorderTraversalHelper(root.right,res)
        res.append(root.val)

# @lc code=end
sol = Solution()
root = TreeNode(1,TreeNode(4,TreeNode(2),TreeNode(5)),TreeNode(3))
res = sol.postorderTraversal(root)


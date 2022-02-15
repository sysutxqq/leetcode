#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #1. 层序遍历，看每一层是不是回文串
        if root == None:
            return True
        elif root.left == None or root.right == None:
            if root.left == root.right:
                return True
            return False
        else:
            curLevelNode = [root]
            numCurLevelNode = 1
            while(curLevelNode):
                subRes = []
                while(numCurLevelNode != 0):
                    curNode = curLevelNode.pop(0)
                    if curNode == None:
                        subRes.append(None)
                        numCurLevelNode -= 1
                        continue
                    curLevelNode.append(curNode.left)
                    curLevelNode.append(curNode.right)
                    subRes.append(curNode.val)
                    numCurLevelNode -= 1
                
                tmpRes = subRes[:]
                tmpRes.reverse()
                if tmpRes != subRes:
                    return False

                tmpNum = 0
                for x in curLevelNode:
                    if x == None:
                        tmpNum += 1
                if tmpNum == len(curLevelNode):
                    break
                numCurLevelNode = len(curLevelNode)

        return True
        #2. 右子树翻转，看和左子树是不是一样
        # if root == None:
        #     return True
        # elif root.left == None or root.right == None:
        #     if root.left == root.right:
        #         return True
        #     return False
        # else:
            # rightRoot = [root.right]
            # transferRight = root.right
            # while(rightRoot):
            #     currNode = rightRoot.pop(0)
            #     if currNode.left or currNode.right:
            #         currNode.left,currNode.right = currNode.right,currNode.left

            #         if currNode.left and currNode.right:
            #             rightRoot.append(currNode.left)                 
            #             rightRoot.append(currNode.right)
            #         elif currNode.left:
            #             rightRoot.append(currNode.left)
            #         elif currNode.right:
            #             rightRoot.append(currNode.right)
            # self.transferTree(root.right)
            # res = self.cmpTree(root.left,root.right)
            # return res

    #比较两棵树是否一样
    def cmpTree(self,leftTree:TreeNode,rightTree:TreeNode)->bool:
        if rightTree == None or leftTree == None:
            if rightTree == leftTree:
                return True
            else:
                return False
        if rightTree.val == leftTree.val:
            return self.cmpTree(rightTree.left,leftTree.left) and self.cmpTree(rightTree.right,leftTree.right)
        return False                                                                                                                                                                                                                                                                                                                  
    
    #递归翻转树结构
    def transferTree(self,root:TreeNode)->TreeNode:
        if root == None:
            return
        else:
            tmpNode = root.left
            root.left = root.right
            root.right = tmpNode
            self.transferTree(root.right)
            self.transferTree(root.left)


    #     #3. 递归
    #     return self.isSymmetricHelper(root,root)
        
    # def isSymmetricHelper(self,leftRoot:TreeNode,rightRoot:TreeNode)->bool:
    #     if leftRoot == None and rightRoot == None:
    #         return True
    #     elif leftRoot == None or rightRoot == None:
    #         return False
    #     elif leftRoot.val == rightRoot.val:
    #         return self.isSymmetricHelper(leftRoot.left,rightRoot.right) and self.isSymmetricHelper(leftRoot.right,rightRoot.left)
    #     return False


# @lc code=end

sol = Solution()
root = TreeNode(1,TreeNode(2,None,TreeNode(3,None,None)),TreeNode(2,None,TreeNode(3,None,None)))
res = sol.isSymmetric(root)


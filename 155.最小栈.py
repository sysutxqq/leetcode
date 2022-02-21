#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
import math


class MinStack:

    def __init__(self):
        self.stack = []
        # self.min = math.inf
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        # if len(self.stack) == 0:
        #     self.min = val
        # else:
        #     self.min = min(self.min,val)
        # self.stack.append(val)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if tmp == self.minStack[-1]:
            self.minStack.pop()
        # tmp = self.stack.pop()
        # if tmp <= self.min:
        #     if self.stack:
        #         self.min = min(self.stack)
        #     else:
        #         self.min = math.inf

    def top(self) -> int:
        tmp = self.stack[-1]
        return tmp

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


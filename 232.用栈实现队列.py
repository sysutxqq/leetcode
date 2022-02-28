#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start

class MyQueue:

    def __init__(self):
        # self.queue = []
        self.stackA = []  ##作为输入栈
        self.stackB = []   ##作为输出栈

    def push(self, x: int) -> None:
        # self.queue.append(x)
        self.stackA.append(x)

    def pop(self) -> int:
        # tmp = self.queue[0]
        # self.queue = self.queue[1:]
        # return tmp
        if len(self.stackB) == 0:
            while(self.stackA):
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

    def peek(self) -> int:
        # return self.queue[0]
        if len(self.stackB) == 0:
            while(self.stackA):
                self.stackB.append(self.stackA.pop())
        return self.stackB[-1]

    def empty(self) -> bool:
        # if len(self.queue) == 0:
        #     return True
        # return False
        if len(self.stackA) == 0 and len(self.stackB) == 0:
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end


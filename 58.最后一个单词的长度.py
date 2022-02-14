#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
from time import process_time_ns
from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        resList = s.split(" ")
        removeList = filter(lambda x:x!="",resList)
        newList = list(removeList)
        return len(newList[-1])
# @lc code=end
s = "Hello World"
sol = Solution()
res = sol.lengthOfLastWord(s)


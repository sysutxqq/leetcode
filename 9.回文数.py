#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
from typing import SupportsAbs


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        resStr = 0
        soureNum = x
        while x > 0:
            base = x % 10 
            temp = x//10
            resStr = resStr*10 + base
            x = temp
        if resStr == soureNum:
            return True
        return False
# @lc code=end
s = Solution()
res = s.isPalindrome(121)
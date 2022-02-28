#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start

class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while(num >= 10):
            res = 0
            while(num > 0):
                tmp = num % 10
                res = tmp + res
                num = num // 10
            num = res
        return res

# @lc code=end
sol = Solution()
res = sol.addDigits(38)


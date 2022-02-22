#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        count = 32
        res = 0
        while(count > 0):
            res = res<<1
            res = res + n&1
            n = n>>1
            count = count - 1
        return res
# @lc code=end


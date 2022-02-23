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
            res = res<<1  # 0左移1位还是0
            tmp = n&1  #取最后一位
            res = res|tmp  
            n = n>>1
            count = count - 1
        return res
# @lc code=end


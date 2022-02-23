#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 32
        res = 0
        while(count > 0):
            tmp = n&1
            if tmp == 1:
                res += 1
            n = n>>1
            count -= 1
        return res
# @lc code=end


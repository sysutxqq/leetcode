#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            if n&(n-1) == 0:
                return True
        return False
        # while(n>0):
        #     if n == 1:
        #         return True
        #     tmp = n%2
        #     if tmp != 0:
        #         return False
        #     n = n//2
        # return False
# @lc code=end
n = 16
sol = Solution()
res = sol.isPowerOfTwo(n)


#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        while(1):
            if n not in nums:
                nums.append(n)
                res = self.isHappyHelper(n)
                if res == 1:
                    return True
                else:
                    n = res
            else:
                return False
        return False
        
    def isHappyHelper(self,n:int)->int:
        res = 0
        while(n > 0):
            tmp = n % 10
            res += tmp*tmp
            n = n//10
        return res
# @lc code=end

sol = Solution()
res = sol.isHappy(19)
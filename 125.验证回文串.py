#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        s = s.lower()
        for x in s:
            if x >= '0' and x <= '9':
                tmp.append(x)
            elif (x >= 'a' and x <= 'z') or x >= 'A' and x <= 'Z':
                tmp.append(x)
        res = tmp[:]
        tmp.reverse()
        if res == tmp:
            return True
        return False
# @lc code=end

s = "A man, a plan, a canal: Panama"
sol = Solution()
res = sol.isPalindrome(s)
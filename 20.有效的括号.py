#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s)%2==1:
        #     return False
        # left = []
        # right = []
        # dict = {'(':')','[':']','{':'}'}
        # for i in range(0,len(s)):
        #     if s[i] in dict.keys():
        #         left.append(s[i])
        #     elif s[i] in dict.values():
        #         if len(left) != 0:
        #             if s[i] == dict[left[-1]]:
        #                 tmp = left.pop()
        #             else:
        #                 return False
        #         else:
        #             return False
        # if len(left) != 0:
        #     return False
        # return True
        for i in range(0,len(s)//2):
            if '()' in s or '[]' in s or '{}' in s:
                s = s.replace('()','')
                s = s.replace('[]','')
                s = s.replace('{}','')
        if len(s) == 0:
            return True
        else:
            return False
# @lc code=end
s = Solution()
res = s.isValid("((")

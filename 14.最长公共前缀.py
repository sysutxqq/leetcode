#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # subStr = ''
        # lengths=[]
        # for i in strs:
        #     lengths.append(len(i))
        # minLength = min(lengths)
        # endFalg = False
        # for i in range(0,minLength):
        #     for j in range(0,len(strs)):
        #         if strs[j][i] == strs[0][i]:
        #             continue
        #         else:
        #             endFalg = True
        #             break
        #     if endFalg:
        #         break
        #     else:
        #         subStr = subStr + strs[0][i]
        # return subStr
        minStr =  min(strs)
        maxStr = max(strs)
        for i,x in enumerate(minStr):
            if x != maxStr[i]:
                return minStr[:i]
        return minStr
# @lc code=end
s = Solution()
strs = ["flower","flow","flight"]
subStr = s.longestCommonPrefix(strs)

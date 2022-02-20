#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numDict = {}
        # for num in nums:
        #     numDict[num] = numDict.get(num,0) + 1
        # for k in numDict.keys():
        #     if numDict[k] == 1:
        #         return k
        res = 0
        for num in nums:
            res = res^num
        return res
# @lc code=end


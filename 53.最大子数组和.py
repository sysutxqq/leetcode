#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from ast import Num
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            maxSumSubList = nums[0]
            res = nums[0]
            for i in range(1,len(nums)):
                tmpSum = maxSumSubList + nums[i]
                maxSumSubList = max(tmpSum,nums[i]) #前i个数的最大和
                if res < maxSumSubList:
                    res = maxSumSubList
            return res
# @lc code=end
s = Solution()
res = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

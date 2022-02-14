#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #solution 1
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     for i in range(0,len(nums)):
        #         if nums[i] < target:
        #             if i == len(nums) - 1:
        #                 return i + 1
        #             continue
        #         else:
        #             return i
        # return 0
        #solution 2
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

# @lc code=end


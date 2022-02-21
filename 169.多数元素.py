#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        flagNum = nums[0]
        countFlag = 1
        for i in range(1,len(nums)):
            if nums[i] == flagNum:
                countFlag += 1
            else:
                countFlag -= 1
                if countFlag == 0:
                    flagNum = nums[i]
                    countFlag = 1
        return flagNum
            

# @lc code=end


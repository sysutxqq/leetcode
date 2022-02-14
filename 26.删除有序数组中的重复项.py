#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        smallIndex = 0
        bigIndex = smallIndex + 1
        while(bigIndex < len(nums)):
            if nums[smallIndex] >= nums[bigIndex]:
                bigIndex = bigIndex + 1
            else:
                smallIndex = smallIndex + 1
                tmp = nums[bigIndex]
                nums[bigIndex] = nums[smallIndex]
                nums[smallIndex] = tmp
                bigIndex = bigIndex + 1
        newLength = 0
        for i in range(0,len(nums) - 1):
            if nums[i] < nums[i+1]:
                newLength = newLength + 1
            else:
                break
        return newLength + 1

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
res = s.removeDuplicates(nums)
 # @lc code=end


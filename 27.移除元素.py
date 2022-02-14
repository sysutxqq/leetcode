#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        targetIndex = 0
        while targetIndex < len(nums) - 1:
            swapIndex = targetIndex + 1
            if nums[targetIndex] == val:
                while nums[swapIndex] == val and swapIndex < len(nums) -1:
                    swapIndex = swapIndex + 1
                
                tmp = nums[swapIndex]
                nums[swapIndex] = nums[targetIndex]
                nums[targetIndex] = tmp

            targetIndex = targetIndex + 1
        newlength = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                newlength = newlength + 1
            else:
                break
        return newlength
# @lc code=end
nums = [1,2,3]
s = Solution()
res = s.removeElement(nums,3)

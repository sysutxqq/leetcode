#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res
# @lc code=end


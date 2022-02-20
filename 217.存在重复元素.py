#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dictNum = {}
        # for num in nums:
        #     dictNum[num] = dictNum.get(num,0) + 1
        # for k in dictNum.keys():
        #     if dictNum[k] >= 2:
        #         return True
        # return False
        setNum = set(nums)
        return len(setNum) < len(nums)
# @lc code=end


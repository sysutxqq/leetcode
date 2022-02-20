#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from re import I
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictNum = {}
        for num in nums:
            dictNum[num] = dictNum.get(num,0) + 1
        for kv in dictNum.keys():
            indexStart = nums.index(kv)
            if dictNum[kv] >= 2:
                for j in range(dictNum[kv]):
                    
                    try:
                        indexEnd =  nums.index(kv,indexStart + 1,indexStart + k + 1)
                    
                    except ValueError:
                        continue
                    else:
                        return True

        return False
        
# @lc code=end
sol = Solution()
nums = [1,2,3,1]
sol.containsNearbyDuplicate(nums,3)

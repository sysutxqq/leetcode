#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        startPos = True
        subStr = ""
        preIndex = 0
        endIndex = 0
        for i in range(len(nums)):
            #判断最后一个区间
            if i == len(nums) - 1:
                if startPos:
                    subStr = str(nums[i]) 
                    res.append(subStr)
                else:
                    subStr = subStr + "->" + str(nums[i])
                    res.append(subStr)
                break
            #重新开始一个区间    
            if startPos:
                subStr = str(nums[i])
                startPos = False
                preIndex = i
                endIndex = i
            #判断区间是否结束
            if nums[i + 1] == nums[i] + 1:
                endIndex += 1
                continue
            else:
                if preIndex != endIndex:
                    subStr = subStr + "->" + str(nums[i])
                else:
                    subStr = str(nums[i])
                res.append(subStr)
                startPos = True
        return res
# @lc code=end
nums = [0,1,2,4,5,7]
sol = Solution()
res =sol.summaryRanges(nums)

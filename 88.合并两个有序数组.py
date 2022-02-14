#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1.insert(i,nums2[i])
                nums1.pop()
        else:
            # indexOfinsert = 0
            # lenOfres = m
            # for i in range(n):
            #     while nums2[i] >= nums1[indexOfinsert] and indexOfinsert < lenOfres:
            #         indexOfinsert += 1
            #     nums1.insert(indexOfinsert,nums2[i])
            #     nums1.pop()
            #     lenOfres += 1
            #     indexOfinsert += 1
            while n > 0:
                if nums1[m-1] > nums2[n-1] and m != 0:
                    nums1[m+n-1] = nums1[m-1]
                    m -= 1
                else:
                    nums1[m+n-1] = nums2[n-1]
                    n -= 1
                
# @lc code=end
sol = Solution()
nums1 = [2,0]
nums2 = [1]
sol.merge(nums1,1,nums2,1)


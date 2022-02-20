#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1,len(prices)):
           maxProfit = max(maxProfit,prices[i] - minPrice)
           minPrice = min(prices[i],minPrice)
        return maxProfit
# @lc code=end


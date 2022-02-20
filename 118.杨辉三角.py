#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:       
        res = []
        for i in range(numRows):
            now = [1] * (i + 1)  ## 值为1的基础list,第几行长度就为多少
            if i >= 2:  #第三行之后
                for j in range(1,i):
                    now[j] = pre[j-1] + pre[j]
            res.append(now)
            pre = now
        return res

        
# @lc code=end


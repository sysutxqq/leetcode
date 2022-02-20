#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex + 1):
            preZero = [0] + res
            backZero = res + [0]
            tmpRes = []
            for j in range(i + 1):
                tmpRes.append(preZero[j] + backZero[j])
            res = tmpRes
        return res
        
        # res = []
        # for i in range(rowIndex + 1):
        #     now = [1] * (i + 1)
        #     if i >= 2:
        #         for j in range(1,i):
        #             now[j] = pre[j-1] + pre[j]
        #     res.append(now)
        #     pre = now
        # return res[rowIndex]
# @lc code=end
sol = Solution()
res = sol.getRow(3)


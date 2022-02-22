#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while(columnNumber > 0):
            remain = (columnNumber-1) % 26
            tmp = chr(remain + ord('A'))
            res.append(tmp)
            columnNumber = (columnNumber-1) // 26
        res.reverse()
        fianlRes = ''.join(res)
        return fianlRes
# @lc code=end
num = 701
sol = Solution()
res = sol.convertToTitle(num)


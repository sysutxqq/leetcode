#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # columnTitleList = list(columnTitle)
        # res = 0
        # power = 1
        # while(columnTitleList):
        #     tmp = columnTitleList.pop()
        #     tmpNum = ord(tmp) - ord('A') + 1
        #     res = tmpNum * power + res
        #     power = 26 * power
        # return res
        res = 0
        for s in columnTitle:
            tmpNum = ord(s) - ord('A') + 1
            res = 26 * res + tmpNum
        return res
# @lc code=end
s = "AB"
sol = Solution()
res =sol.titleToNumber(s)

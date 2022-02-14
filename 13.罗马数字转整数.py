#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1}
        dict['V'] = 5
        dict['X'] = 10
        dict['L'] = 50
        dict['C'] = 100
        dict['D'] = 500
        dict['M'] = 1000
        res = 0
        point = 0
        #solute with range
        if len(s) == 1:
            return dict[s[0]]
            
        it = iter(range(0,len(s)-1))
        for i in it:
            i
            if dict[s[i]] >= dict[s[i+1]]:
                res = res + dict[s[i]]
            else:
                res = res + dict[s[i+1]] - dict[s[i]]
                try:
                    i = next(it)
                except StopIteration:
                    point = i + 1
                    break
            point = i
        if point == len(s) - 1:
            return res
        else:
            return res + dict[s[-1]]
        #solute with while 
        # i = 0 
        # while i < len(s) - 1:
        #     if dict[s[i]] >= dict[s[i+1]]:
        #         res = res + dict[s[i]]
        #         i= i + 1
        #     else:
        #         res = res + (dict[s[i+1]] - dict[s[i]])
        #         i = i + 2
        #     point = i
        # if point == len(s):
        #     return res
        # else:
        #     return res + dict[s[point]]

# @lc code=end
s = Solution()
subStr = "D"
res = s.romanToInt(subStr)

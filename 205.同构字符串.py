#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        setFort = set()  #存t的值，判断是否存在多对1
        relationMap = {}  #存s->t的映射关系
        for i in range(len(s)):
            if s[i] in relationMap.keys():
                #存在一对多的情况
                if t[i] != relationMap[s[i]]:
                    return False
            else:
                #存在多对一的情况
                if t[i] in setFort:
                    return False
                setFort.add(t[i])
                relationMap[s[i]] = t[i]
        return True
# @lc code=end


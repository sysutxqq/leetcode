#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
from operator import le


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        relation = {}
        strList = s.split(" ")
        setS = set()   #存s中的值
        if len(pattern) != len(strList):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] not in relation.keys():
                if strList[i] in setS:  #存在多对1的情况
                    return False
                relation[pattern[i]] = strList[i]
                setS.add(strList[i])
            else:
                #存在一对多的情况
                if strList[i] != relation[pattern[i]]:
                    return False
        return True
# @lc code=end


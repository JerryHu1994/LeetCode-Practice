class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, ret = {}, -1
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for key, val in dic.items():
            if val != 1:    continue
            ind = s.find(key)
            if (ret == -1) or (ind < ret):   ret = ind 
        return ret
        
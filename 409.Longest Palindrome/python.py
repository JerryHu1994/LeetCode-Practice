class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ret = 0
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            if dic[i] >= 2:
                dic[i] -= 2
                ret += 2
        for i in dic:
            if dic[i] == 1:
                return ret + 1
        return ret
        
        
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, ret = bin(n), 0
        for i in s[2:]:
            if i == '1':    ret += 1
        return ret
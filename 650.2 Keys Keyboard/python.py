class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        p = 2
        while n > 1:
            while n % p == 0:
                ret += p
                n = n/p
            p += 1
        return ret
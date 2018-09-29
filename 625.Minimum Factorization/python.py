class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1 or a == 0:    return a
        mul, ret = 1, 0
        for i in range(9, 1, -1):
            while a%i == 0:
                ret = ret + i*mul
                mul *= 10
                a = a/i
        return 0 if a > 10 or ret > 2**31-1 else ret
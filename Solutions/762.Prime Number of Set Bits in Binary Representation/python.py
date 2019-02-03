class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = set([2,3,5,7,11,13,17,19,23])
        ret = 0
        for i in range(L, R+1):
            if bin(i)[2:].count("1") in primes: ret += 1
        return ret
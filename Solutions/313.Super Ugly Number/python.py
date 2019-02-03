from heapq import *
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ptrs, ugly = [0]*len(primes), [1]*n
        for i in range(1, n):
            curr_min = float("inf")
            for j in range(len(primes)):
                curr_min = min(curr_min, primes[j]*ugly[ptrs[j]])
            for j in range(len(primes)):
                # for all next product equal to the min, update all of them
                if primes[j]*ugly[ptrs[j]] == curr_min:
                    ptrs[j] += 1
            ugly[i] = curr_min
        return ugly[-1]
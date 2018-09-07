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
# recursion
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:  return 0
        for i in range(2,n/2+1):
            if n%i == 0:
                return i + self.minSteps(n/i)
        return n
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:  return 1
        ret = 10
        for i in range(2, n+1):
            if i == 10: return ret
            curr = 1
            for j in range(i):
                curr *= (9 if j == 0 else 10-j)
            ret += curr
        return ret
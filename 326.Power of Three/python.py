class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:  return False
        ret = math.log10(n)/math.log10(3)
        return int(ret) == ret
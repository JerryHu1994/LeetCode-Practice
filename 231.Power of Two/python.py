class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:  return False
        if n==1:    return True
        if not n%2:
            return self.isPowerOfTwo(n/2)
        else:
            return False
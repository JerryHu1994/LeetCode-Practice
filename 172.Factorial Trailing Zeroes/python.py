class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret, curr = 0, n
        while curr/5 >= 1:
            curr = curr/5
            ret += curr
        return ret
        
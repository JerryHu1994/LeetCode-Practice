class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.floor((-1+math.sqrt(1+8*n))/2))
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==0:    return 0
        same, diff = 0, k
        for i in range(n-1):
            same, diff = diff, same*(k-1) + diff*(k-1)
            
        return same+diff
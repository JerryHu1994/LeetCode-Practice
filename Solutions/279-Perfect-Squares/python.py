class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sol = [float("inf")]*(n+1)
        sol[0] = 0
        sol[1] = 1
        for i in xrange(2,n+1):
            j = 1
            while j*j <= i:
                sol[i] = min(sol[i], sol[i-j*j] + 1)
                j+=1
        return sol[n]
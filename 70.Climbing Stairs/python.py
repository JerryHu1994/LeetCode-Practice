class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        li = n*[0]
        li[0] = 1
        if n==1:    return li[-1]
        li[1] = 2
        if n ==2: return li[-1]
        for i in range(2,n):
            li[i] = li[i-1] + li[i-2]
        return li[-1]
        
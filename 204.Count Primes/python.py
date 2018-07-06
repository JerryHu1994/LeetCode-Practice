class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:    return 0
        ret = [1]*n
        ret[0] = 0
        ret[1] = 0
        for i in xrange(2,n):
            if ret[i] == 1:
                for j in xrange(2, (n-1)//i+1):
                    ret[i*j] = 0  
        return sum(ret)
        
        
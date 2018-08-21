class Solution(object):
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]*(n)
        for i in range(1,n):
            fac[i] = fac[i-1]*i
        ret = []
        num = [str(i) for i in range(1, n+1)]
        k -= 1 
        for i in range(n, 0, -1):
            div = k/fac[i-1]
            k = k%fac[i-1]
            ret.append(num[div])
            num.pop(div)
        return "".join(ret)
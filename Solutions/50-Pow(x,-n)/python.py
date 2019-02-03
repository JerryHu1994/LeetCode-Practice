class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:   return 1/self.myPow(x,-n)
        if n==1:    return x
        if n==0:    return 1
        if n % 2==1:
            temp = self.myPow(x, n/2)
            return temp * temp * x
        else:
            temp = self.myPow(x, n/2)
            return temp*temp
        
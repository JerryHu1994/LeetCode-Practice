class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1:    return x
        left, right = 0, x
        mid = 0
        while True:
            mid = (left+right)/2
            if mid*mid<=x and (mid+1)*(mid+1)>x:    return mid
            if mid*mid < x: 
                left=mid
            else:
                right=mid
        return mid
            
                
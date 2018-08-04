class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = (left+right)/2
            if mid**2 == num:
                return True
            elif mid **2 > num:
                right = mid-1
            else:
                left = mid+1
        return False
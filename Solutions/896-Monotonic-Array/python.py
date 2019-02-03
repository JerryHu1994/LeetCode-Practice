class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sign = None
        for i in range(1, len(A)):
            diff = A[i] - A[i-1]
            if diff == 0:
                continue
            else:
                if sign == None:
                    sign = diff
                elif diff*sign < 0:
                    return False
        return True
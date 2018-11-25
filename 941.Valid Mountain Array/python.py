class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:  return False
        l = len(A)
        left, right = 0, l-1
        ind = 0
        while ind+1 < l and A[ind] < A[ind+1]:  ind += 1
        if ind == 0 or ind == l-1:    return False
        while ind+1 < l and A[ind] > A[ind+1]:  ind += 1
        return ind == l-1
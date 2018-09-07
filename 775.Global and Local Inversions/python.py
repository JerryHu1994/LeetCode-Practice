class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        currmin = N
        for i in range(N-1, 0, -1):
            currmin = min(currmin, A[i])
            if i >= 2 and A[i-2] > currmin:
                return False
        return True
                
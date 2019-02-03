class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        totalsum, n = sum(A), len(A)
        if n == 0:  return 0
        currsum = 0
        for ind, val in enumerate(A):
            currsum += ind*val
        bestsum = None
        for i in range(n):
            numtocut = A[-1-i]
            currsum = currsum + totalsum - numtocut - (n-1)*numtocut
            bestsum = currsum if bestsum == None or currsum > bestsum else bestsum
        return bestsum
            
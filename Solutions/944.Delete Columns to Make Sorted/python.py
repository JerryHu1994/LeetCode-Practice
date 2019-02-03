class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ret = 0
        l = len(A)
        width = len(A[0])
        for i in range(width):
            valid = True
            for j in range(l-1):
                if A[j][i] > A[j+1][i]:
                    valid = False
                    break
            if not valid:   ret += 1
        return ret
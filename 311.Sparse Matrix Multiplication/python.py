class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ah, aw, bw = len(A), len(A[0]), len(B[0])
        ret = [[0]*bw for a in xrange(ah)]
        for i in xrange(ah):
            for j in xrange(aw):
                if A[i][j]:
                    for k in xrange(bw):
                        ret[i][k] += A[i][j]*B[j][k]
        return ret
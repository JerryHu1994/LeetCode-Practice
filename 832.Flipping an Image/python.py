class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # flip
        for rowidx in range(len(A)):
            A[rowidx] = A[rowidx][::-1]
        for rowidx in range(len(A)):
            for colidx in range(len(A[0])):
                A[rowidx][colidx] = 1 if A[rowidx][colidx] == 0 else 0
        return A
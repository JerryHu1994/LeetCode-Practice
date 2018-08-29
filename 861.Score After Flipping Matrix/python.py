class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # make sure leftmost bit is 1
        for rowidx in range(len(A)):
            if A[rowidx][0] == 0:
                # toggle the row
                for col in range(len(A[rowidx])):
                    A[rowidx][col] = 1 if A[rowidx][col] == 0 else 0
        transpose = zip(*A)
        height = len(A)
        for i in range(1, len(transpose)):
            if sum(transpose[i]) <= height//2:
                # toggle the col
                for j in range(height):
                    A[j][i] = 1 if A[j][i] == 0 else 0
        return sum([int(''.join([str(j) for j in i]), 2) for i in A])
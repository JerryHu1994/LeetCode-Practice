class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lena, lenb = len(A), len(B)
        dp = [[0]*lena for i in range(lenb)]
        # fill the last row
        for i in range(lena):
            if B[-1] == A[i]:
                dp[-1][i] = 1 
        # fill the column
        for i in range(lenb):
            if B[i] == A[-1]:
                dp[i][-1] = 1 
        for i in range(lenb-2, -1, -1):# row
            for j in range(lena-2, -1, -1): # col
                if A[j] == B[i]:
                    dp[i][j] += dp[i+1][j+1] + 1
        ret = 0
        for i in dp:
            ret = max(max(i), ret)
        return ret
            
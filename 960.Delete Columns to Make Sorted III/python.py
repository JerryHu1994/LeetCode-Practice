class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s, l = len(A), len(A[0])
        dp = [1]*l #
        for i in range(1, l):
            for j in range(i):
                if all([A[k][i] >= A[k][j]  for k in range(s)]):
                    dp[i] = max(dp[i], dp[j]+1)
        return l - max(dp)
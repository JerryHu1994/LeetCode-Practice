class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        culsum = [0]
        N = len(A)
        for i in A:
            culsum.append(float(culsum[-1]+i)) # to find average for [i, j], we use (culsum[j] - culsum[i])/(j-1)
        dp = [0]*N
        for i in range(len(A)):
            dp[i] = (culsum[N] - culsum[i])/(N - i)
        for i in range(2, K+1):
            for k in range(len(A)):
                currmax = 0
                for j in range(k+1, len(A)):
                    currmax = max(currmax, (culsum[j] - culsum[k])/(j-k) + dp[j])
                dp[k] = currmax
        return dp[0]
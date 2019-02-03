class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for i in range(n+1)]
        for leng in range(1, n):
            for i in range(1, n+1):
                target = i+leng
                if target > n:  break
                best = float("inf")
                
                for pivot in range(i, target+1):
                    curr = pivot
                    if pivot == i:
                        curr += dp[pivot+1][target]
                    elif pivot == target:
                        curr += dp[i][pivot-1]
                    else:
                        curr += max(dp[pivot+1][target], dp[i][pivot-1])
                    best = min(best, curr)
                dp[i][target] = best
        return dp[1][n]
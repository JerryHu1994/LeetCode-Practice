class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = [0, 1, 4] + [float("inf")]*target
        for i in range(3, target+1):
            k = i.bit_length()
            if i == 2**k - 1:
                dp[i] = k
                continue
            for j in range(k-1):
                dp[i] = min(dp[i], dp[i-2**(k-1)+2**j]+k-1+j+2) # stop at A(k-1) -> R -> dp[] -> r
            if 2**k - 1 - i < i:
                dp[i] = min(dp[i], dp[2**k-1-i]+k+1) # stop at A(k) -> R -> dp[]
        return dp[target]
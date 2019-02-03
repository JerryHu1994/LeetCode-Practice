class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        dp = [None]*(amount+1)
        for i in coins:
            if i >= len(dp):    continue
            dp[i] = 1
        for i in range(1, amount+1):
            if dp[i] == None:
                minamount = float("inf")
                for c in coins:
                    if 0<=i-c<len(dp) and dp[i-c] != None:
                        minamount = min(minamount, dp[i-c]+1)
                dp[i] = minamount if minamount != float("inf") else None
        return dp[-1] if dp[-1] != None else -1
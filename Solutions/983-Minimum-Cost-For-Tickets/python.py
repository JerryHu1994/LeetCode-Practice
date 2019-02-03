class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        maxdays = days[-1]
        dp = [0]*(maxdays+1)
        s = set(days)
        for i in range(1, maxdays+1):
            if i not in s:
                dp[i] = dp[i-1]
                continue
            one_day = costs[0] + (dp[i-1] if i-1 >= 0 else 0)
            seven_day = costs[1] + (dp[i-7] if i-7 >= 0 else 0)
            thirty_day = costs[2] + (dp[i-30] if i-30 >= 0 else 0)
            dp[i] = min([one_day, seven_day, thirty_day])
        return dp[-1]
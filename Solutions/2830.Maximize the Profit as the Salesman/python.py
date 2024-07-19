class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0]*n
        sorted_offers = sorted(offers, key=lambda x: (x[0], x[1]))
        curridx = 0
        for ind in range(n):
            if ind > 0:
                dp[ind] = max(dp[ind-1], dp[ind])
            while curridx < len(sorted_offers) and ind == sorted_offers[curridx][0]:
                currstart, currend, currprice = sorted_offers[curridx]
                if currstart == 0:
                    dp[currend] = max(dp[currend], currprice)
                else:
                    dp[currend] = max(dp[currend], dp[currstart-1]+currprice)
                curridx += 1
        return dp[-1]
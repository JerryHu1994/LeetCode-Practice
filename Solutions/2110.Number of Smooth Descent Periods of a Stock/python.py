class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        currstart = -1
        ans = 0
        for ind, val in enumerate(prices):
            if ind == 0:
                ans += 1
            else:
                if val == prices[ind-1]-1:
                    ans += ind - currstart
                else:
                    ans += 1
                    currstart = ind - 1
        return ans
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides = sorted(rides)
        l = len(rides)
        startlist = [r[0]   for r in rides]
        @lru_cache(None)
        def dp(index):
            if index == l:  return 0
            start, end, tip = rides[index]
            ans = dp(index+1) #do not pick this passenger
            insert = bisect.bisect_left(startlist, end)
            ans = max(ans, end-start+tip+dp(insert))
            return ans
        return dp(0)
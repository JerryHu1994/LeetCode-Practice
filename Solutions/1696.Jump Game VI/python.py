class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        pq = []
        heapq.heappush(pq, (-nums[0], 0))
        for i in range(1, len(nums)):
            while pq[0][1] < i-k:
                heapq.heappop(pq)
            dp[i] = dp[pq[0][1]] + nums[i]
            heapq.heappush(pq, (-dp[i], i))
        print (dp)  
        return dp[-1]
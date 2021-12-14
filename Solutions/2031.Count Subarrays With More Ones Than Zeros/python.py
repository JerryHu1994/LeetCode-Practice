class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        ans = amt = dp = 0
        mp = defaultdict(int, {0:1})
        for n in nums:
            amt += 1 if n else -1
            dp += mp[amt-1] if n else -mp[amt]
            mp[amt] += 1
            ans += dp
        return ans % 1000000007
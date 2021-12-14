class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        for n in nums:
            ans += cnt[n-k]
            ans += cnt[n+k]
            cnt[n] += 1
        return ans
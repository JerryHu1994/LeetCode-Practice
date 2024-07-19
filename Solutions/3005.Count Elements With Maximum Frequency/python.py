class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_freq = max(cnt.values())
        ans = 0
        for item in cnt.values():
            if item == max_freq:
                ans += 1
        return ans*max_freq
        
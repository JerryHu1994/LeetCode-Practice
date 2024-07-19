class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        left, right = 0, 0
        cnt = defaultdict(int)
        while right < len(nums):
            cnt[nums[right]] += 1
            if cnt[nums[right]] > k:
                while left < right:
                    cnt[nums[left]] -= 1
                    if nums[left] == nums[right]:
                        left += 1
                        break
                    left += 1
            right += 1
            ans = max(ans, right-left)
        return ans
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, count_zero, n = 0, 0, 0, len(nums)
        ans = 0
        while right < n:
            while right < n:
                if nums[right] == 0:
                    count_zero += 1
                right += 1
                if count_zero > k:
                    break
                ans = max(ans, right - left)
            while left <= right and left < n and nums[left] != 0:
                left += 1
            count_zero -= 1
            left += 1
        return ans
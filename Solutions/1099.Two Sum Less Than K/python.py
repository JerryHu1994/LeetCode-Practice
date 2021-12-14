class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left, right = 0, len(nums)-1
        currsum = nums[left] + nums[right]
        ans = -1
        while left < right:
            currsum = nums[left] + nums[right]
            if currsum < k:
                left += 1
                ans = max(ans, currsum)
            else:
                right -= 1
        return ans
            
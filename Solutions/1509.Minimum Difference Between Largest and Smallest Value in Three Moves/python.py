class Solution:
    def minDifference(self, nums: List[int]) -> int:
        unchanged = len(nums) - 3
        sorted_nums = sorted(nums)
        if unchanged <= 1:  return 0
        ans = sys.maxsize
        for i in range(0, len(nums)-unchanged+1):
            ans = min(ans, sorted_nums[i+unchanged-1] - sorted_nums[i])
        return ans
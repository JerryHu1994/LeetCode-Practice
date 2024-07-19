class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1:  return 1
        ans = 0
        left, right = 0, 1
        curr = nums[right]
        while right < len(nums):
            if nums[right] == nums[right-1]:
                ans += int((right-left+1)*(right-left)/2)
                left = right
            right += 1
        ans += int((right-left+1)*(right-left)/2)
        return ans
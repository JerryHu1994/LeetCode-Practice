class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]>nums[j]:
                        ans = max(ans, (nums[i]-nums[j])*nums[k])
        return ans
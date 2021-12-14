class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currsum = nums[0]
        ans = currsum
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                currsum += nums[i]
            else:
                currsum = nums[i]
            ans = max(ans, currsum)
        return ans
                
    
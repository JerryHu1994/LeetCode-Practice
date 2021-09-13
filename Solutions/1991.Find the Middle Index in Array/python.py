class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        currleft = 0
        for i in range(len(nums)):
            if currleft == total_sum - currleft - nums[i]:
                return i
            currleft += nums[i]
        return -1
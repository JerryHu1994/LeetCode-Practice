class Solution:
    def check(self, nums: List[int]) -> bool:
        decrease_count = 0
        sort = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                decrease_count += 1
        return decrease_count == 0 or (decrease_count == 1 and nums[0] >= nums[-1])
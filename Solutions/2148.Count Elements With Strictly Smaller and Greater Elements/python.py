class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        return len([i for i in nums   if i != min_num and i != max_num])
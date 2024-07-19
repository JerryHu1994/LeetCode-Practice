class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_num, second_num = float('inf'), float('inf')
        for i in nums[1:]:
            if i < min_num:
                min_num, second_num = i, min_num
            elif i < second_num:
                second_num = i
        return sum([nums[0], min_num, second_num])
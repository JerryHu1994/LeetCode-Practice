class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = sum([n for n in nums if n < 10])
        double_digit = sum([n for n in nums if n >= 10])
        return single_digit != double_digit
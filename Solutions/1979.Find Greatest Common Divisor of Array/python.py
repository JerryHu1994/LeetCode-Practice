class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)
        curr_divisor = min_num
        curr_div = 1
        while curr_div < min_num:
            if min_num % curr_div == 0:
                curr_divisor = min_num/curr_div
                if max_num % curr_divisor == 0:
                    return int(curr_divisor)
            curr_div += 1
        return 1
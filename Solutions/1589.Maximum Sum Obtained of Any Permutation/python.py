class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        frequency_list = [0]*(len(nums)+1)
        for start, end in requests:
            frequency_list[start] += 1
            frequency_list[end+1] -= 1
        for k in range(1, len(nums)):
            frequency_list[k] += frequency_list[k-1]
        sorted_nums = sorted(nums, reverse=True)
        ans = 0
        num_idx = 0
        for freq in sorted(frequency_list[:-1], reverse=True):
            ans += freq*sorted_nums[num_idx]
            num_idx += 1
        return int(ans%(math.pow(10, 9)+7))
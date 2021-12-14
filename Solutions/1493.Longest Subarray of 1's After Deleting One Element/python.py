class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        last_zero = []
        last_zero.append(-1)
        lastidx = -1
        for ind, n in enumerate(nums):
            if n == 1:
                last_zero.append(last_zero[-1])
            else:
                last_zero.append(lastidx)
                lastidx = ind
        last_zero = last_zero[1:]
        for ind, n in enumerate(nums):
            if n == 1:
                ans = max(ans, ind-last_zero[ind]-1)
            else:
                ans = max(ans, ind-last_zero[ind]-1)
        return ans
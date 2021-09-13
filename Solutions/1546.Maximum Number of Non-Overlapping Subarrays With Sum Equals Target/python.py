class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        curr = 0
        res = 0
        seen = set([0])
        for ind,n in enumerate(nums):
            curr += n
            if curr - target in seen:
                res += 1
                seen = set()
            seen.add(curr)
        return res
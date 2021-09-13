class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = [0]
        currsum = 0
        for n in nums:
            currsum += n
            prefix.append(currsum)
        return abs(max(prefix) - min(prefix))
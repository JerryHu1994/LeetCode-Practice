class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        maxval = max(nums)
        numset = set(nums)
        ans = original
        while ans <= maxval:
            if ans in numset:
                ans = ans*2
            else:
                return ans
        return ans
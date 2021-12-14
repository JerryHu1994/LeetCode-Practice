class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -sys.maxsize
        currmin = nums[0]
        for n in nums[1:]:
            if n > currmin:
                ans = max(n - currmin, ans)
            currmin = min(currmin, n)
        return -1 if ans == -sys.maxsize else ans
            
        
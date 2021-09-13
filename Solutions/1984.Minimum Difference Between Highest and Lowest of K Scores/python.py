class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 0:  return 0
        nums = sorted(nums)
        between = k - 1
        diffs = []
        for i in range(1,len(nums)):
            diffs.append(nums[i]-nums[i-1])
        ans = None
        for i in range(0,len(nums)-between):
            currsum = sum(diffs[i:i+between])
            if ans == None or currsum < ans:
                ans = currsum
        return ans
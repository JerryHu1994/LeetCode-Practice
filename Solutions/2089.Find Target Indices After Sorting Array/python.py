class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        pos = bisect.bisect_left(nums, target)
        ans = []
        for i in range(pos, len(nums)):
            if nums[i] == target:
                ans.append(i)
            else:
                break
        return ans
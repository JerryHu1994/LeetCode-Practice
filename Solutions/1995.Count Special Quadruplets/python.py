class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        diff = defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                diff[nums[j]-nums[i]].append(i)
        ans = 0
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                ans += sum([k > j for k in diff[nums[i]+nums[j]]])
        return ans
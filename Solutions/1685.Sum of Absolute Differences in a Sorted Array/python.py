class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        currsum, totallen = 0, len(nums)
        for n in nums:   currsum += n - nums[0]
        ans.append(currsum)
        for i in range(1, len(nums)):
            currdiff = nums[i] - nums[i-1]
            currsum = currsum - (totallen -i)*currdiff + i*currdiff
            ans.append(currsum)
        return ans
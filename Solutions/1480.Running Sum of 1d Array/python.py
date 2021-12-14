class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        curr_sum = 0
        for n in nums:
            curr_sum += n
            ans.append(curr_sum)
        return ans
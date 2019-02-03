class Solution(object):

    def helper(self, templist, nums, start):
        Solution.result.append(templist)
        for i in range(start,len(nums)):
            val = nums[i]
            self.helper(templist+[val], nums, i+1)
    
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.result = []
        sortedarr = sorted(nums)
        self.helper([], nums, 0)
        return Solution.result
        
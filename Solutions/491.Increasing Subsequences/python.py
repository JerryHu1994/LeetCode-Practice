class Solution(object):
    def helper(self, nums, holder):
        if len(holder) >= 2:
            self.ret.append(holder)
        s = set()
        for ind, val in enumerate(nums):
            if val in s:    continue
            if len(holder) == 0 or val >= holder[-1]:
                s.add(val)
                self.helper(nums[ind+1:], holder + [val])
    
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret = []
        self.helper(nums, [])
        return self.ret
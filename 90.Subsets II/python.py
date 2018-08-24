class Solution(object):
    def helper(self, remaining, currlist):
        if len(remaining) == 0:
            return currlist
        nexts = set([tuple(i) for i in currlist])
        first = remaining[0]
        for l in currlist:
            curr = l + [first]
            nexts.add(tuple(curr))
        return self.helper(remaining[1:], [list(i) for i in nexts])
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        return self.helper(nums, [[]])
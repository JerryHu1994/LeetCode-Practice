class Solution(object):
    def helper(self, nums, depth, pos, s):
        found = False
        for num in nums:
            currdepth, currpos, currval = int(num[0]), int(num[1]), int(num[2])
            if currdepth == depth and currpos in pos:
                self.helper(nums, depth+1, [currpos*2, currpos*2-1], s+currval)
                found = True
        if not found:
            self.ret += s
                
        
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [str(n) for n in nums]
        self.ret = 0
        self.helper(nums, 1, [1], 0)
        return self.ret
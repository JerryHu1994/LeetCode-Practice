class Solution(object):
    
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        ret = []
        for i,v in enumerate(nums):
            temp = self.permute(nums[:i] + nums[i+1:])
            # append first element to lists
            for j in temp:
                j.append(v)
            ret += temp
        return ret
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == None:
                continue
            n, curr = i, 0
            while nums[n] != None:
                curr += 1
                temp = nums[n]
                nums[n] = None
                n = temp
            
            ret = max(ret, curr)
        return ret
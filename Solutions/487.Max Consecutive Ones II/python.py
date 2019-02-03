class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = -1, 0
        zeroidx, ret = None, 0
        while r < len(nums):
            if nums[r] == 0:
                # no zero encountered so far
                if zeroidx == None:
                    zeroidx = r
                    if r-l > ret:   ret = r-l
                    r += 1
                else:
                    l = zeroidx
                    zeroidx = None
            else:
                if r-l > ret:   ret = r-l
                r += 1
        return ret
                
                
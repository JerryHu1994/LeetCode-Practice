class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:  return 0
        curr, currlen = 0, 1
        ret = 1
        while curr+1 <= len(nums)-1:
            if nums[curr+1] > nums[curr]:
                currlen += 1
                ret = max(ret, currlen)
            else:
                currlen = 1
            curr = curr+1
        return ret
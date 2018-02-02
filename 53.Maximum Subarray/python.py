class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumlist, ret = [nums[0]], nums[0]
        for i in range(1,len(nums)):
            toadd = nums[i] if sumlist[i-1] < 0 else sumlist[i-1]+nums[i]
            ret = max(ret, toadd)
            sumlist.append(toadd)
        return ret
        
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(1,len(nums),1):
            if nums[i-1] == nums[i]:
                return nums[i]
            
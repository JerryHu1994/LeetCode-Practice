class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while i+1 != nums[i]:
                currnum = nums[i]
                if nums[currnum-1] == currnum:  break
                nums[i], nums[currnum-1] = nums[currnum-1], currnum #swamp the val
        ret = []
        for ind,val in enumerate(nums):
            if ind+1 != val:
                ret.append(val)
        return ret
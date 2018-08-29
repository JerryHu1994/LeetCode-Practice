class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            while nums[i] != i+1 and nums[i] < l and nums[i] > 0:
                val = nums[i]
                if nums[val-1] == nums[i]:  break
                nums[i], nums[val-1] = nums[val-1], nums[i]
        for i in range(l):
            if nums[i] != i+1:
                return i+1
        return l+1
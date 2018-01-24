class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right, ret = [], [], []
        curr = 1
        for i in range(len(nums)):
            left.append(curr)
            curr = curr*nums[i]
        curr = 1
        for i in range(len(nums)):
            right.insert(0,curr)
            curr = curr*nums[len(nums)-1-i]
        for i in range(len(nums)):
            ret.append(left[i]*right[i])
        return ret
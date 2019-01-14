class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        ans = [1]*l
        curr_p = 1
        for i in range(l):
            ans[i] = curr_p
            curr_p *= nums[i]
        curr_p = 1
        for i in range(l-1, -1, -1):
            ans[i] *= curr_p
            curr_p *= nums[i]
        return ans
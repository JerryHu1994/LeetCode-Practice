class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:   return
        ind = len(nums)-1
        while ind > 0 and nums[ind] <= nums[ind-1]:
            ind -= 1
        if ind == 0:
            # not possible
            nums[:] = sorted(nums)
            return
        ind = ind-1
        i = ind + 1
        val = nums[ind]
        while i < len(nums)-1 and not nums[i] > val >= nums[i+1]:
            i += 1
        # swap ind and i
        nums[ind], nums[i] = nums[i], nums[ind]
        nums[ind+1:] = nums[ind+1:][::-1]
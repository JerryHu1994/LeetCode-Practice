class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] == val:
                # switch with right
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return len(nums) - nums.count(val)
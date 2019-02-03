class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 1
        while left < len(nums) and right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            while right - left > 2:
                nums.pop(left)
                right -= 1
            left, right = right, right+1
        return len(nums)
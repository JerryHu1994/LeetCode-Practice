class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)/2
            midval = nums[mid]
            if midval == nums[right]:
                right -= 1
            elif midval > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]
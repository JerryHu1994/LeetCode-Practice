class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)/2
            # on the left branch
            if nums[mid] >= nums[l] and nums[mid]>nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        if target < nums[0]:    return 0
        if target > nums[-1]:   return len(nums)
        while l <= r:
            mid = (l+r)/2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if mid + 1 < len(nums) and nums[mid+1] <= target:
                    l = mid + 1
                else:
                    return mid+1
            else:
                r = mid -1
        return l + 1
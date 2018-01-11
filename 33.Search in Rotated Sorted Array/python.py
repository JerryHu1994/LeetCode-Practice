class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:    return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target: return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[left] <= target and nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
        return -1
                
                
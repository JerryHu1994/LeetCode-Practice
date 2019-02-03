class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 or len(nums)==1:    return len(nums)
        left, right = 0, 1
        while True:
            while nums[right] == nums[left]:
                del nums[right]
                if left >= len(nums) or right >= len(nums):    break
            left += 1
            right += 1
            if left >= len(nums) or right >= len(nums):    break
        return len(nums)
        
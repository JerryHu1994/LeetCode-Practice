class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right, currprod, ret = 0, 0, nums[0], 0
        while left < len(nums):
            if currprod >= k:
                # move left
                if right - 1 >= left:
                    ret += right - left
                currprod = currprod/nums[left]
                left += 1 
            else:
                # move right
                right += 1
                if right >= len(nums):  break
                currprod *= nums[right]
        # add the remaining
        for i in range(len(nums)-left):
            ret += i+1
        return ret
        
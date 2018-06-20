class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum, curr = [0]*len(nums), 0
        for i in range(1,len(nums)):
            curr += nums[i-1]
            left_sum[i] = curr
        curr = 0
        right_sum = [0]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            curr += nums[i+1]
            right_sum[i] = curr
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
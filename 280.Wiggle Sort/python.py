class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:  return
        sortednums = sorted(nums)
        nums[0] = sortednums[0]
        for i in range(1, len(sortednums), 2):
            if i+1 < len(sortednums):
                nums[i], nums[i+1] = sortednums[i+1], sortednums[i]
        if len(sortednums)%2 == 0:
            nums[i] = sortednums[i]
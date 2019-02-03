class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:  return
        sortednums = sorted(nums)
        first_half = sortednums[:len(nums)/2]
        second_half = sortednums[len(nums)/2:]
        if len(first_half) < len(second_half):
            first_half.append(second_half.pop(0))
        for i in range(len(nums)):
            if i%2 == 1:
                nums[i] = second_half.pop()
            else:
                nums[i] = first_half.pop()
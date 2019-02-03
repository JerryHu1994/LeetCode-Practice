class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        ind = 0
        while ind <= right:
            if nums[ind] == 0:
                if ind == left:
                    ind+=1
                    left+=1
                else:
                    nums[ind], nums[left] = nums[left], 0
                    left += 1
            elif nums[ind] == 1:
                ind += 1
            else:
                nums[right], nums[ind] = 2, nums[right]
                right -= 1
        
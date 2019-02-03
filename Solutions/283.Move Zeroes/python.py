class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = -1 if nums[0] == 0 else 0
        right, l = 1, len(nums)
        while right < l:
            if nums[right] != 0:
                #swap left+1 with right
                temp = nums[right]
                nums[right] = nums[left+1]
                nums[left+1] = temp
                left+=1
                right+=1
            else:
                right +=1 
                
            
        
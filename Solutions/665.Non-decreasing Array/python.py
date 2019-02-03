class Solution(object):
    
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]: count += 1
            if count > 1 or ((i>=1 and nums[i-1] > nums[i+1]) and (i<len(nums)-2 and nums[i] > nums[i+2])):
                return False
        return True
                
        
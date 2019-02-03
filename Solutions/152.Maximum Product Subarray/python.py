class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:    return nums[0]
        poslist = [0]*len(nums)
        neglist = [0]*len(nums)
        poslist[0] = nums[0] if nums[0] > 0 else 0
        neglist[0] = nums[0] if nums[0] < 0 else 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                poslist[i] = 0
                neglist[i] == 0
            elif nums[i] > 0:
                poslist[i] = poslist[i-1]*nums[i] if poslist[i-1]>0 else nums[i]
                neglist[i] = neglist[i-1]*nums[i] if neglist[i-1]<0 else 0
            else:
                poslist[i] = neglist[i-1]*nums[i] if neglist[i-1]<0 else 0
                neglist[i] = poslist[i-1]*nums[i] if poslist[i-1]>0 else nums[i]
        return max(poslist)
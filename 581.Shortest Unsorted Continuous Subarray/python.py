class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        culmin, culmax = [0]*l, [0]*l
        culmin[-1], culmax[0] = nums[-1], nums[0]
        for i in range(l-2, -1, -1):
            culmin[i] = min(nums[i], culmin[i+1])
        for i in range(1, l):
            culmax[i] = max(nums[i], culmax[i-1])
        # find the front and end point
        front, end = None, None
        for i in range(l):
            if nums[i] != culmin[i]:
                front = i-1
                break
        for i in range(l-1, -1, -1):
            if nums[i] != culmax[i]:
                end = i+1
                break
        return 0 if front == None or end == None else end - front - 1
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        currsum = sum([nums[i] for i in range(k)])
        maxsum = currsum
        for i in range(k,len(nums)):
            currsum = currsum - nums[i-k] + nums[i]
            maxsum = max(currsum, maxsum)
        return float(maxsum)/float(k)
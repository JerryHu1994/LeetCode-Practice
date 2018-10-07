class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sums = []
        for i in range(len(nums)-k+1):
            sums.append(sum(nums[i:i+k]))
        leftmax, rightmax = [0]*len(sums), [0]*len(sums)
        curr, idx = float("-inf"), 0
        for i in range(len(sums)):
            if sums[i] > curr:
                idx = i
                curr = sums[i]
            leftmax[i] = idx
        curr, idx = float("-inf"), 0
        curr = float("-inf")
        for i in range(len(sums)-1, -1, -1):
            if sums[i] > curr:
                idx = i
                curr = sums[i]
            rightmax[i] = idx
        ret, maxsum = [], float("-inf")
        for i in range(k, len(nums)-2*k+1):
            currsum = sums[leftmax[i-k]] + sums[i] + sums[rightmax[i+k]]
            if currsum > maxsum:
                maxsum = currsum
                ret = [leftmax[i-k], i, rightmax[i+k]]
        return ret
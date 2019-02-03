class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnts = [1]*len(nums)
        l = [1]*len(nums)
        mx = 0
        ret = 0
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if l[j] + 1 == l[i]:
                        cnts[i] += cnts[j]
                    if l[j] + 1 > l[i]:
                        l[i] = l[j] + 1
                        cnts[i] = cnts[j]
            if mx == l[i]:
                ret += cnts[i]
            elif mx < l[i]:
                ret = cnts[i]
                mx = l[i]
        return ret
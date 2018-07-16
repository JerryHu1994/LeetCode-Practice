class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l = len(nums)
        rank = sorted([(val, ind) for ind, val in enumerate(nums)])
        nums[rank[-1][1]] = "Gold Medal"
        if l == 1:  return nums
        nums[rank[-2][1]] = "Silver Medal"
        if l == 2:  return nums
        nums[rank[-3][1]] = "Bronze Medal"
        if l == 3:  return nums
        r = 4
        for i in rank[0:-3][::-1]:
            nums[i[1]] = str(r)
            r+=1
        return nums
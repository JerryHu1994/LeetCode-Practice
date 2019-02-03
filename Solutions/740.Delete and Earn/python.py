class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        prev = None
        take = 0 # if we take curr, how much score we get
        avoid = 0# if we avoid curr, how much score we get
        for i in sorted(cnt):
            if i-1 != prev:
                take, avoid = cnt[i]*i + max(take, avoid), max(take, avoid) # does not matter since it is not adjacent
            else:
                take, avoid = avoid+cnt[i]*i, max(take, avoid) 
            prev = i
        return max(avoid, take)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic, curr, ret = {0:1}, 0, 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr - k in dic:
                ret += dic[curr - k]
            if curr in dic:
                dic[curr] += 1
            else:
                dic[curr] = 1
        return ret
        
            
        
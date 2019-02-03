class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        ret = 0
        for i in dic:
            if i+1 in dic:
                curr = dic[i] + dic[i+1]
                ret = max(ret, curr)
        return ret
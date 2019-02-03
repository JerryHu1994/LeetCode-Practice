class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        degree = 0
        for ind, val in enumerate(nums):
            if val in dic:
                dic[val][1] = ind
                dic[val][2] += 1
            else:
                dic[val] = [ind, ind, 1]
            degree = max(degree, dic[val][2])
        ret = float("inf")
        for val, li in dic.items():
            if li[2] == degree:
                ret = min(ret, li[1]-li[0]+1)
        return ret
        
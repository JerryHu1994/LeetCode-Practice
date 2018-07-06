class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        ret = []
        for i in range(1, len(nums)+1, 1):
            if not i in s:
                ret.append(i)
        return ret
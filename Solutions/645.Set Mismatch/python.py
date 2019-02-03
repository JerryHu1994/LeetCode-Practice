class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        ret = []
        for i in nums:
            if i in s:
                ret.append(i)
                continue
            s.add(i)
        for i in range(1,len(nums)+1):
            if not i in s:
                ret.append(i)
                break
        return ret
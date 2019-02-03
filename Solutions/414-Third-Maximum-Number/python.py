class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        first = [None]*3
        for i in nums:
            for ind, val in enumerate(first):
                if val == None or i > val:
                    first.insert(ind, i)
                    first.pop()
                    break
        return first[-1] if first[2] != None else first[0]
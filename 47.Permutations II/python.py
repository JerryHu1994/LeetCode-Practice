class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        ret = []
        dup = set()
        for i,v in enumerate(nums):
            if v in dup:
                continue
            else:
                dup.add(v)
            temp = self.permuteUnique(nums[:i] + nums[i+1:])
            # append first element to lists
            for j in temp:
                j.append(v)
            ret += temp
        return ret
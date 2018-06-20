class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count, ret = collections.Counter(nums), 0
        for i in count:
            if (k > 0 and i+k in count) or (k == 0 and count[i]>=2):
                ret += 1
        return ret
            
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for i in nums:
            dic[i] += 1
            if dic[i] > len(nums)/2:
                return i
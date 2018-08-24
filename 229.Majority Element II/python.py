class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = collections.defaultdict(int)
        ret = []
        for i in nums:
            dic[i] += 1
            if i not in ret and dic[i] > len(nums)/3:
                ret.append(i)
        return ret 
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = collections.defaultdict(list)
        for ind, val in enumerate(nums):
            dic[val].append(ind)
        for key in dic:
            for i in range(len(dic[key])-1):
                if dic[key][i+1] - dic[key][i] <= k:
                    return True
        return False
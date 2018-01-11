class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for ind, val in enumerate(nums):
            if target-val in hashtable:  return [hashtable[target-val], ind]
            hashtable[val] = ind
        return
                 
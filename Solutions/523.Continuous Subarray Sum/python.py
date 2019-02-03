class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:   return False
        if k == 0:
            return True if sum(nums) == 0 else False
        culsum = [0]*(len(nums)+1)
        dic = collections.defaultdict(int)
        dic[0] = 0
        for i in range(1, len(nums)+1):
            culsum[i] = culsum[i-1] + nums[i-1]
            if culsum[i]%k in dic:
                if i - dic[culsum[i]%k] > 1:
                    return True
            else:
                dic[culsum[i]%k] = i
        return False
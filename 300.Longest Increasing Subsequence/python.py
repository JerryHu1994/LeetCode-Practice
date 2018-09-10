#O(n^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:    return 0
        l = len(nums)
        dp = [1]*l
        for i in range(1, l):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

# O(nlogn)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        taillist = []
        for n in nums:
            insert_idx = bisect.bisect_left(taillist, n)
            if insert_idx == len(taillist):
                taillist.append(n)
            else:
                taillist[insert_idx] = n
        return len(taillist)
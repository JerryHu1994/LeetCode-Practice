
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        summap = collections.defaultdict(int)
        summap[0] = 1
        for x in nums:
            curr = collections.defaultdict(int)
            for y in summap:
                curr[y+x] += summap[y]
                curr[y-x] += summap[y]
            summap = curr
        return summap[S]
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [[0 for i in range(2001)] for j in range(len(nums))]
        dp[0][nums[0] + 1000] += 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1,len(nums)):
            for j in range(-1000, 1001):
                if dp[i-1][j+1000] != 0:
                    dp[i][j+1000-nums[i]] += dp[i-1][j+1000]
                    dp[i][j+1000+nums[i]] += dp[i-1][j+1000]
        return 0 if S>1000 else dp[len(nums)-1][S+1000]
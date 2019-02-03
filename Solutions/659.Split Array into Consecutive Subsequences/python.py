class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = collections.Counter(nums)
        dp = collections.defaultdict(int)
        for n in nums:
            if counter[n] == 0:
                continue
            elif dp[n] > 0:
                dp[n+1] += 1
                dp[n] -= 1
            elif counter[n+1] > 0 and counter[n+2] > 0:
                counter[n+1] -= 1
                counter[n+2] -= 1
                dp[n+3] += 1
            else:
                return False
            counter[n] -= 1
        return True
        
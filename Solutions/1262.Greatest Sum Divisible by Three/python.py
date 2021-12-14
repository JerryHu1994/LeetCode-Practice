class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0]*l for i in range(3)]
        for ind,n in enumerate(nums):
            curr_mod = n%3
            if ind == 0:
                dp[curr_mod][ind] = n
            else:
                for i in range(3):
                    if i == curr_mod:
                        dp[i][ind] = max(dp[0][ind-1] + n, dp[i][ind-1])
                    else:
                        dp[i][ind] = max(dp[(i+3-curr_mod)%3][ind-1] + n, dp[i][ind-1]) if dp[(i+3-curr_mod)%3][ind-1] != 0 else dp[i][ind-1]
        return dp[0][-1]

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums = [1] + nums + [1]
        dp = [[0]*(l+2) for i in range(l+2)] # dp[i][j] represents the answer for nums[i:j] inclusive
        for length in range(1, l+1):
            for i in range(1, l+1):
                start, end = i, i+length-1
                if end > l: continue
                for j in range(start, end+1):
                    dp[start][end] = max(dp[start][end], nums[j]*nums[start-1]*nums[end+1]+dp[start][j-1]+dp[j+1][end])                
        print (dp)
        return dp[1][l]
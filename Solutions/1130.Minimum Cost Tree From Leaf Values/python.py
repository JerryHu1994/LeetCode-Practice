class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        l = len(arr)
        dp = [[0]*l for i in range(l)]
        for y in range(1, l):
            startx, starty = 0, y
            while starty<l:
                currsmall = sys.maxsize
                for k in range(startx, starty):
                    currsmall = min(currsmall, max(arr[startx:k+1])*max(arr[k+1:starty+1])+dp[startx][k]+dp[k+1][starty])
                dp[startx][starty] = currsmall
                startx += 1
                starty += 1
        return dp[0][l-1]
            
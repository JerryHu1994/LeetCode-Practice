class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        height, width = len(matrix), len(matrix[0])
        dp = [[0]*width for i in range(height)]
        ans = 0
        currsum = 0
        for i in range(height):
            currsum += matrix[i][0]
            dp[i][0] = currsum
        ans += currsum
        currsum = 0
        for i in range(width):
            currsum += matrix[0][i]
            dp[0][i] = currsum
        ans += currsum
        if matrix[0][0] == 1:   ans -= 1
        for i in range(1, height):
            for j in range(1, width):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
        for i in range(1, height):
            for j in range(1, width):
                if matrix[i][j] == 1:
                    for k in range(1, min(i,j)+2):
                        curr = dp[i][j]
                        upper = dp[i-k][j] if i - k >=0 else 0
                        left = dp[i][j-k] if j-k>= 0 else 0
                        upperleft = dp[i-k][j-k] if j-k>=0 and i-k>=0 else 0
                        if curr-upper-left+upperleft == k*k:
                            ans += 1
        return ans
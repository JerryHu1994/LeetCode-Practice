class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        presum = [[0]*w for i in range(h)]
        containsx = [[False]*w for i in range(h)]
        ans = 0
        for i in range(h):
            for j in range(w):
                left_up_sum = presum[i-1][j-1] if i>0 and j>0 else 0
                left_sum = presum[i][j-1] if j > 0 else 0
                up_sum = presum[i-1][j] if i > 0 else 0
                curr_num = 0
                if grid[i][j] == "X":
                    curr_num = 1
                elif grid[i][j] == "Y":
                    curr_num = -1
                presum[i][j] = left_sum + up_sum - left_up_sum + curr_num
                left_contains_x = containsx[i][j-1] if j > 0 else False
                up_contains_x = containsx[i-1][j] if i > 0 else False
                containsx[i][j] = left_contains_x or up_contains_x or grid[i][j] == "X"
                if containsx[i][j] and presum[i][j] == 0:
                    ans += 1
        return ans
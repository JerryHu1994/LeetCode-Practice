class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        half = (int)(math.floor(n/2))
        cnt_y = defaultdict(int)
        cnt_other = defaultdict(int)
        counted = [[False]*n    for i in range(n)]
        # count y
        for i in range(half):
            cnt_y[grid[i][i]] += 1
            counted[i][i] = True
        for i in range(half):
            cnt_y[grid[i][n-1-i]] += 1
            counted[i][n-1-i] = True
        for i in range(half+1):
            cnt_y[grid[half+i][half]] += 1
            counted[half+i][half] = True
        for i in range(n):
            for j in range(n):
                if not counted[i][j]:
                    cnt_other[grid[i][j]] += 1
        ysum = half*3+2
        othersum = n*n - ysum
        li = [0,1,2]
        ans = float('inf')
        for y_num in li:
            for other_num in li:
                if y_num != other_num:
                    ans = min(ysum - cnt_y[y_num] + othersum - cnt_other[other_num], ans)
        return ans
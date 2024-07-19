class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left, right, top, bottom = -1, -1, -1, -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if left == -1:
                        left, right, top, bottom = j, j, i, i
                    else:
                        left, right, top, bottom = min(j, left), max(j, right), min(i, top), max(i, bottom)
        return 0 if left == -1 else (right-left+1)*(bottom-top+1)
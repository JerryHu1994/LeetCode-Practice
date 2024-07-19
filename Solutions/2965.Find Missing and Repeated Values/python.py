class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        visited = set()
        n = len(grid)
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in visited:
                    visited.add(grid[i][j])
                else:
                    a = grid[i][j]
        for i in range(1, n*n+1):
            if i not in visited:
                return [a, i]
        return [a, b]

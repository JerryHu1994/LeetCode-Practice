class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vector = []
        for sub in grid:    vector += sub
        vector.sort()
        median = vector[len(vector)//2]
        res = 0
        for n in reversed(vector):
            if abs(n-median) % x != 0:
                return -1
            res += abs(n-median) // x
        return res
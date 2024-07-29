class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        diag = 0
        for rect in dimensions:
            curr_diag = rect[0]**2 + rect[1]**2
            if curr_diag > diag:
                diag = curr_diag
                ans = rect[0]*rect[1]
            elif curr_diag == diag:
                if rect[0]*rect[1] > ans:
                    ans = rect[0]*rect[1]
        return ans


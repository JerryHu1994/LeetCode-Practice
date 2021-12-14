class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        height, width = len(points), len(points[0])
        prelist = points[0]
        
        def cal_left(arr):
            curr = [0]*width
            curr[0] = arr[0]
            for i in range(1, width):   curr[i] = max(curr[i-1]-1, arr[i])
            return curr
        def cal_right(arr):
            curr = [0]*width
            curr[-1] = arr[-1]
            for i in range(width-2, -1, -1):    curr[i] = max(curr[i+1]-1, arr[i])
            return curr
        for i in range(1, height):
            leftarr, rightarr, currarr = cal_left(prelist), cal_right(prelist), [0]*width
            for j in range(width):
                currarr[j] = points[i][j] + max(leftarr[j], rightarr[j])
            prelist = currarr
        return max(prelist)
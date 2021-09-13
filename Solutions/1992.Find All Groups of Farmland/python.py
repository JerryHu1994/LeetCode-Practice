class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        height, width = len(land), len(land[0])
        for y in range(height):
            for x in range(width):
                if (x == 0 or land[y][x-1] == 0) and (y == 0 or land[y-1][x] == 0) and land[y][x] == 1:
                    # find a top left 
                    curry, currx = y, x
                    while curry + 1 < height and land[curry+1][currx] == 1:  curry += 1
                    while currx + 1 < width and land[curry][currx+1] == 1:  currx += 1
                    ans.append([y, x, curry, currx])
        return ans
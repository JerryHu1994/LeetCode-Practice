class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        currmax = 0
        ans = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > currmax:
                currmax = heights[i]
                ans.append(i)
        return ans[::-1]
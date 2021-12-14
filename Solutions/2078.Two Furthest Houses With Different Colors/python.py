class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        fromfirst, fromlast = 0, len(colors)-1
        while colors[fromfirst] == colors[-1]:
            fromfirst += 1
        while colors[0] == colors[fromlast]:
            fromlast -= 1
        return max(fromlast, len(colors)-1-fromfirst)
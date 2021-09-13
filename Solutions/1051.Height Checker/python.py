class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_arr = sorted(heights)
        return sum([heights[i] != sorted_arr[i] for i in range(len(heights))])
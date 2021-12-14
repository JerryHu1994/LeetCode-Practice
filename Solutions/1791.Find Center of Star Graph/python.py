class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = defaultdict(int)
        for from_point, to_point in edges:
            count[from_point] += 1
            count[to_point] += 1
            if count[from_point] > 1:   return from_point
            if count[to_point] > 1: return to_point
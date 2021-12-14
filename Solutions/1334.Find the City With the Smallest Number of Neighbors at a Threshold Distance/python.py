class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis_map = [[float("inf")]*n for i in range(n)]
        for from_node, to_node, weight in edges:
            dis_map[from_node][to_node] = weight
            dis_map[to_node][from_node] = weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis_map[i][j] = min(dis_map[i][j], dis_map[i][k] + dis_map[k][j])
        ans = 0
        best_cnt = float("inf")
        for i in range(n):
            cnt = 0
            for j in range(n):
                if j != i and dis_map[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= best_cnt:
                best_cnt, ans = cnt, i
        return ans
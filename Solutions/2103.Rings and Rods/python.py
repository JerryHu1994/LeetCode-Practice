class Solution:
    def countPoints(self, rings: str) -> int:
        rod_set = defaultdict(set)
        for i in range(0, len(rings), 2):
            color = rings[i]
            index = int(rings[i+1])
            rod_set[index].add(color)
        ans = 0
        for k, v in rod_set.items():
            if len(v) == 3:
                ans += 1
        return ans
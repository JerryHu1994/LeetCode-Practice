class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for first_city, second_city in roads:
            cnt[first_city] += 1
            cnt[second_city] += 1
        pairs = [(k,cnt[k]) for k in cnt.keys()]
        pairs = sorted(pairs, key=lambda x:x[1], reverse=True)
        ans = 0
        for num in range(n, 0, -1):
            if n-num >= len(pairs):   break
            ans += num*pairs[n-num][1]
        return ans
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        dic = defaultdict(int)
        for candie in candies:
            dic[candie] += 1
        for i in range(k):
            dic[candies[i]] -= 1
            if dic[candies[i]] == 0:
                del dic[candies[i]]
        ans = len(dic)
        for i in range(k, len(candies)):
            dic[candies[i]] -= 1
            dic[candies[i-k]] += 1
            if dic[candies[i]] == 0:
                del dic[candies[i]]
            ans = max(ans, len(dic))
        return ans
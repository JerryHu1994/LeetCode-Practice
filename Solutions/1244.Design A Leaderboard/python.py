class Leaderboard:

    def __init__(self):
        self.score = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.score:
            self.score[playerId] = score
        else:
            self.score[playerId] += score

    def top(self, K: int) -> int:
        hq = []
        for p, s in self.score.items():
            heappush(hq, (s, p))
        nlar = heapq.nlargest(K, hq)
        return sum([n[0]    for n in nlar])


    def reset(self, playerId: int) -> None:
        del self.score[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
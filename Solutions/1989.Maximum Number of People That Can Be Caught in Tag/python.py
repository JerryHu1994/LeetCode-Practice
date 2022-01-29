class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        it_index = []
        for i in range(len(team)):
            if team[i] == 1:    it_index.append(i)
        heapq.heapify(it_index)
        ans = 0
        for ind, val in enumerate(team):
            if val == 0:
                lower, upper = max(0, ind - dist), min(len(team)-1, ind + dist)
                while len(it_index) > 0:
                    smallest = heapq.heappop(it_index)
                    if smallest >= lower and smallest <= upper:
                        ans += 1
                        break
                    elif smallest > upper:
                        heapq.heappush(it_index, smallest)
                        break
        return ans
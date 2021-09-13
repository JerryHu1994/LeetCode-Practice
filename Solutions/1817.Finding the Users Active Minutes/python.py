class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic = defaultdict(set)
        for userid, time in logs:
            dic[userid].add(time)
        res = [0]*(k+1)
        for key, val in dic.items():
            res[len(val)] += 1
        return res[1:]
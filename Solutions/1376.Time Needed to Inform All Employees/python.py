class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        queue = []
        ans = 0
        queue.append((headID, 0))
        dic = defaultdict(list)
        for employnum, employmanager in enumerate(manager):
            if employmanager != -1:
                dic[employmanager].append(employnum)
        while len(queue):
            currind, currtime = queue.pop()
            ans = max(ans, currtime)
            if currind in dic:
                for nextemploy in dic[currind]:
                    queue.append((nextemploy, currtime+informTime[currind]))
        return ans
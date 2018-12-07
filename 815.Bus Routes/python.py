class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                dic[stop].append(i)
        q = [S]
        visited = [False]*len(routes)
        cnt = 0
        if S == T:  return cnt
        while len(q):
            print q
            size = len(q)
            cnt += 1
            while size > 0:
                curr = q.pop(0)
                for bus in dic[curr]:
                    if visited[bus]:    continue
                    visited[bus] = 1
                    for nextstop in routes[bus]:
                        if nextstop == T:   return cnt
                        q.append(nextstop)
                size -= 1
        return -1
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        dic = collections.defaultdict(list)
        for dis in dislikes:
            dic[dis[0]].append(dis[1])
            dic[dis[1]].append(dis[0])
        visited, group = [False]*(N+1), [None]*(N+1)
        for i in range(1, N+1):
            if visited[i]:    continue
            queue = [i]
            currgroup = True
            while len(queue):
                nextqueue = []
                for j in queue:
                    if not visited[j]:
                        visited[j] = True
                        group[j] = currgroup
                        nextqueue.extend(dic[j])
                    elif group[j] != currgroup:
                        return False
                currgroup = not currgroup
                queue = nextqueue
        return True
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        dic = collections.defaultdict(list)
        tuples = [tuple(i)  for i in stones]
        for i in range(len(tuples)):
            for j in range(i):
                if tuples[i][0] == tuples[j][0] or tuples[i][1] == tuples[j][1]:
                    dic[tuples[i]].append(tuples[j])
                    dic[tuples[j]].append(tuples[i])
        ans = 0
        visited = set()
        while len(dic):
            size = 0
            queue = [next(iter(dic.keys()))]
            visited.add(queue[0])
            while len(queue):
                curr = queue.pop(0)
                for n in dic[curr]:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
                del dic[curr]
                size += 1
            ans += size - 1
        return ans
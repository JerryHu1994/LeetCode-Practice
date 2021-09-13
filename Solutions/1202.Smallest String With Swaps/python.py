class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dic = defaultdict(list)
        for fr, to in pairs:
            dic[fr].append(to)
            dic[to].append(fr)
        visited = set()
        groups = []
        n = len(s)
        for root in range(n):
            if root not in visited and len(dic[root]) > 0:
                group_indices = set([root])
                visited.add(root)
                queue = [root]
                while len(queue)>0:
                    curr = queue.pop()
                    for nextnode in dic[curr]:
                        if nextnode not in group_indices:
                            group_indices.add(nextnode)
                            visited.add(nextnode)
                            queue.append(nextnode)
                groups.append(group_indices)
        
        out = list(s)
        for indices in groups:
            chars = sorted([s[i] for i in indices])
            indices = sorted(indices)
            for i, c in zip(indices, chars):
                out[i] = c
        return ''.join(out)
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodemap = defaultdict(list)
        for from_node, to_node in edges:
            nodemap[from_node].append(to_node)
            nodemap[to_node].append(from_node)
        self.ans = 0
        def dfs(currnode, visited):
            should_walk = hasApple[currnode]
            for nextnode in nodemap[currnode]:
                if nextnode not in visited:
                    visited.add(nextnode)
                    curr_res = dfs(nextnode, visited)
                    if curr_res:    should_walk = True
                    visited.remove(nextnode)
            if should_walk and currnode != 0:
                self.ans += 2
            return should_walk
        dfs(0, set([0]))
        return self.ans
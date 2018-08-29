class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        state = collections.defaultdict(set)
        queue = []
        n = len(graph)
        if n == 0 or len(graph[0]) == 0:  return 0
        finalstate = (1 << n) - 1
        for i in range(n):
            queue.append((i, 1 << i)) # 0010 represents start state of node 2
            state[i].add(1 << i)
        step = 0
        while len(queue):
            currsize = len(queue)
            step += 1
            for i in range(currsize):
                currnode, currstate = queue.pop(0)
                for nextnode in graph[currnode]:
                    nextstate = 1 << nextnode | currstate
                    if nextstate == finalstate: return step # reach the final state
                    if nextstate in state[nextnode]:    continue # duplicated
                    queue.append((nextnode, nextstate))
                    state[nextnode].add(nextstate)
        return -1
        
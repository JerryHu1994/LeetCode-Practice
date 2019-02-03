class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if len(graph) == 0: return False
        colors = [None]*len(graph)
        for j in range(len(graph)):
            if colors[j] != None:   continue
            queue = [j]
            currBool = True
            while len(queue):
                nextqueue = []
                for i in queue:
                    if colors[i] == None:
                        nextqueue.extend(graph[i])
                        colors[i] = currBool
                    elif colors[i] == currBool:
                        continue
                    else:
                        return False
                currBool = not currBool
                queue = nextqueue
        return True
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def helper(self, root):
        if root not in self.dic:
            clone = UndirectedGraphNode(root.label)
            self.dic[root] = clone
        for nei in root.neighbors:
            if nei in self.dic:
                self.dic[root].neighbors.append(self.dic[nei])
                continue
            nei_clone = self.helper(nei)
            self.dic[root].neighbors.append(nei_clone)     
        return self.dic[root]
    
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        self.dic = {}
        return self.helper(node)
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        linear = []
        # check if all elements are true
        for i in grid:  linear += i
        if all(linear): return Node(True, True, None, None, None, None)
        # check if all elements are false
        if all([not i for i in linear]): return Node(False, True, None, None, None, None)
        halfsize = len(grid)/2
        topleftnode = self.construct([grid[i][0:halfsize] for i in range(halfsize)])
        toprightnode = self.construct([grid[i][halfsize:] for i in range(halfsize)])
        bottomleftnode = self.construct([grid[i][0:halfsize] for i in range(halfsize, len(grid))])
        bottomrightnode = self.construct([grid[i][halfsize:] for i in range(halfsize, len(grid))])
        return Node("*", False, topleftnode, toprightnode, bottomleftnode, bottomrightnode)
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
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2
        elif quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            else:
                return quadTree1
        else:
            topleft, topright, bottomleft, bottomright = self.intersect(quadTree1.topLeft, quadTree2.topLeft), self.intersect(quadTree1.topRight, quadTree2.topRight), self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft), self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and topleft.val == topright.val == bottomleft.val == bottomright.val:
                return Node(topleft.val, True, None, None, None, None)
            return Node(None, False, topleft, topright, bottomleft, bottomright)
        return None
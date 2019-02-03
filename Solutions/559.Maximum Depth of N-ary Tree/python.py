"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:    return 0
        childD = [self.maxDepth(i) for i in root.children]
        return 1 if len(childD)==0 else max(childD)+1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from heapq import *
class Solution(object):
    def helper(self, root, target):
        if root == None:
            return
        heappush(self.heapq, (abs(root.val - target), root.val))
        self.helper(root.left, target)
        self.helper(root.right, target)
    
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.heapq = []
        self.helper(root, target)
        ret = []
        for i in range(k):
            ret.append(heappop(self.heapq)[1])
        return ret
        
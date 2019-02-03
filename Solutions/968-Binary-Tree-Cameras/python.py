# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        all nodes below covered, not this node
        all nodes below and this node is covered, no camera on this
        all nodes below and this node is covered, camera on this
        """
        def helper(r):
            if r == None:   return 0, 0, float("inf") 
            L = helper(r.left)
            R = helper(r.right)
            
            dp_1 = L[1]+R[1]
            dp_2 = min(L[2]+min(R[1:]), R[2]+min(L[1:]))
            dp_3 = 1+min(L)+min(R)
            return dp_1, dp_2, dp_3
        return min(helper(root)[1:])
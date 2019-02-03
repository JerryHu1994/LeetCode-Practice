# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root, val):
        if root == None:    return False
        if val - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.helper(root.left, val) or self.helper(root.right, val)
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.s = set()
        return self.helper(root, k)
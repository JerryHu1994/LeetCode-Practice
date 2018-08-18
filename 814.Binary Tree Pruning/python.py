# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:
            return True
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l:   root.left = None
        if r:   root.right = None
        return l and r and (root.val == 0)
    
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.helper(root):
            return None
        else:
            return root
       
        
        
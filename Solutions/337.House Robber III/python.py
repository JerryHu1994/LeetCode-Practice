# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root):
        if root == None:
            return 0, 0
        useleft, notuseleft = self.helper(root.left)
        useright, notuseright = self.helper(root.right)
        useroot = notuseleft + notuseright + root.val
        notuseroot = max(useleft, notuseleft) + max(useright, notuseright)
        return useroot, notuseroot
    
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))
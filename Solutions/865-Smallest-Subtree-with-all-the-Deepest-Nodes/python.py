# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root==None:  return [0, None]
        leftheight, leftret = self.helper(root.left)
        rightheight, rightret = self.helper(root.right)
        if leftheight > rightheight:
            return leftheight+1, leftret
        elif rightheight > leftheight:
            return rightheight+1, rightret
        else:
            return leftheight + 1, root
    
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root)[1]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # returns the sum of tree
    def helper(self, root):
        left = 0 if root.left == None else self.helper(root.left)
        right = 0 if root.right == None else self.helper(root.right)
        self.ret += abs(left-right)
        return left + right + root.val
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:    return 0
        self.ret = 0
        self.helper(root)
        return self.ret
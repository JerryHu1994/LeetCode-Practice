# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:    return 0
        left_sub = self.helper(root.left)
        right_sub = self.helper(root.right)
        left, right = 0, 0
        if root.left and root.left.val == root.val:
            left = left_sub + 1
        if root.right and root.right.val == root.val:
            right = right_sub + 1
        self.ret = max(self.ret, left+right)
        return max(left,right)
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.helper(root)
        return self.ret
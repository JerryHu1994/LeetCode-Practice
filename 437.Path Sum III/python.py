# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, s):
        if root == None:    return 0
        end_here = 1 if root.val == s else 0
        return self.helper(root.left, s-root.val) + self.helper(root.right, s-root.val) + end_here
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:    return 0
        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + self.helper(root, sum)
        
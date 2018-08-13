# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # return whether root is uni,  count of uni trees in root
    def helper(self, root):
        if root == None:
            return True, 0
        leftuni, leftcount = self.helper(root.left)
        rightuni, rightcount = self.helper(root.right)
        if leftuni and rightuni and (root.left == None or root.val == root.left.val) and (root.right == None or root.val == root.right.val):
            return True, 1 + leftcount + rightcount
        return False, leftcount + rightcount
    
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[1]
        
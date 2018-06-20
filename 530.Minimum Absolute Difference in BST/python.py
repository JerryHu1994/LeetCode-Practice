# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:    return float('inf'), float('inf'), float('-inf')
        l_min_d, l_min_val, l_max_val = self.helper(root.left)
        r_min_d, r_min_val, r_max_val = self.helper(root.right)
        return min(root.val-l_max_val, r_min_val-root.val, l_min_d, r_min_d), min(l_min_val, root.val), max(r_max_val, root.val)
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]
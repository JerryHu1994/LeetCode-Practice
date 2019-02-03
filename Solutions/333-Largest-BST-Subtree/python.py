# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if root == None:    return 0, 0, float('-inf'), float('inf')
        l_bst_num, l_curr_tree, l_max_val, l_min_val = self.dfs(root.left)
        r_bst_num, r_curr_tree, r_max_val, r_min_val = self.dfs(root.right)
        curr_tree = l_curr_tree + r_curr_tree + 1 if root.val > l_max_val and root.val < r_min_val else float('-inf')
        print max(l_bst_num, r_bst_num, curr_tree), curr_tree, max(root.val, r_max_val), min(root.val, l_min_val)
        return max(l_bst_num, r_bst_num, curr_tree), curr_tree, max(root.val, r_max_val), min(root.val, l_min_val)
    
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[0]
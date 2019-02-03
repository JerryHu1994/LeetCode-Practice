# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root):
        if root == None:
            return float('inf'), None, None
        min_left, minval_left, maxval_left = self.helper(root.left)
        min_right, minval_right, maxval_right = self.helper(root.right)
        curr_ret = min(min_left, min_right)
        if maxval_left != None:    curr_ret = min(curr_ret, root.val - maxval_left)
        if minval_right != None:    curr_ret = min(curr_ret, minval_right - root.val)
        curr_min = root.val if minval_left == None else minval_left
        curr_max = root.val if maxval_right == None else maxval_right
        return curr_ret, curr_min, curr_max
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]
        
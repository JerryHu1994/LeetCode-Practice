# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:
            return float("-inf"), 0
        left_ret, left_branch = self.helper(root.left)
        right_ret, right_branch = self.helper(root.right)
        ret = max(left_ret, right_ret, left_branch+right_branch+root.val)
        branch = root.val+max(left_branch, right_branch)
        branch = branch if branch>0 else 0
        return ret, branch
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]
        
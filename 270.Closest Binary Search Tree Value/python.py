# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, target):
        if root == None:
            return [None, None]
        if target == root.val:
            return [root.val, 0]
        elif target < root.val:
            l_val, l_dis = self.helper(root.left, target)
            return [root.val, root.val - target] if l_dis == None or root.val - target < l_dis else [l_val, l_dis]
        else:
            r_val, r_dis = self.helper(root.right, target)
            return [root.val, target - root.val] if r_dis == None or target - root.val < r_dis else [r_val, r_dis]
    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.helper(root, target)[0]
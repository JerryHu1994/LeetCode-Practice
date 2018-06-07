# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root == None:
            return None
        left = self.closestValue(root.left, target)
        right = self.closestValue(root.right, target)
        best = None
        if left == None:    
            best = right
        elif right == None:
            best = left
        else:
            best = left if abs(left-target) < abs(right-target) else right
        ret = None
        if best == None:
            ret = root.val
        else:
            ret = root.val if abs(root.val-target) < abs(best-target) else best
        return ret
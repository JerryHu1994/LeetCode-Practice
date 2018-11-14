# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        return 0 if root == None else ((root.val if L<=root.val<=R else 0) + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R))
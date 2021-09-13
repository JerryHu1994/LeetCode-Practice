# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def helper(node):
            if node:
                left_min, left_max = helper(node.left)
                right_min, right_max = helper(node.right)
                self.ans = max(self.ans, node.val-min(left_min, right_min), max(left_max, right_max)-node.val)
                return min(left_min, right_min, node.val), max(left_max, right_max, node.val)
            else:
                return math.inf, -math.inf
        helper(root)
        return self.ans
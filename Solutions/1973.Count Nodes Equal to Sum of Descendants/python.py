# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(rootnode):
            if rootnode == None:
                return 0
            leftsum = helper(rootnode.left)
            rightsum = helper(rootnode.right)
            if rootnode.val == leftsum + rightsum:
                self.ans += 1
            return leftsum + rightsum + rootnode.val
        helper(root)
        return self.ans
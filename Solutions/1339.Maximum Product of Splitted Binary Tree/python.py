# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        totalsum = 0
        def countsum(rootnode):
            if rootnode == None:    return 0
            return countsum(rootnode.left) + countsum(rootnode.right) + rootnode.val
        totalsum = countsum(root)
        self.ret = 0
        def helper(rootnode):
            if rootnode == None:    return 0
            leftsum = helper(rootnode.left)
            rightsum = helper(rootnode.right)
            currsum = leftsum+rightsum+rootnode.val
            self.ret = max(self.ret, (totalsum-currsum)*currsum)
            return currsum
        helper(root)
        return self.ret % (10**9+7)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = [root]
        while len(queue):
            res = sum([n.val for n in queue])
            nextq = []
            for n in queue:
                if n.left != None:  nextq.append(n.left)
                if n.right != None:  nextq.append(n.right)
            queue = nextq
        return res
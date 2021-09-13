# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, currmax, root) -> int:
        if root is None:    return 0
        
        leftcount = self.dfs(max(currmax, root.val), root.left)
        rightcount = self.dfs(max(currmax, root.val), root.right)
        currcount = 1 if root.val >= currmax else 0
        return leftcount + rightcount + currcount
    
    def goodNodes(self, root: TreeNode) -> int:
        if TreeNode is None:    return 0
        return self.dfs(root.val, root)
            
        
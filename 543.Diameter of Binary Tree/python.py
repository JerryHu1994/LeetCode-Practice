# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root):
        if root is None:
            return [0, 0]
        [maxDepthL, maxDiaL] = self.helper(root.left)
        [maxDepthR, maxDiaR] = self.helper(root.right)
        currMaxDepth = max(maxDepthL, maxDepthR) + 1
        currMaxDia = max(maxDiaL,maxDiaR, maxDepthL+maxDepthR+1)
        return [currMaxDepth, currMaxDia]
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:    return 0
        return self.helper(root)[1]-1
        
        
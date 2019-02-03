# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root, presum):
        if root == None:    return presum
        s = self.helper(root.right, presum)
        root.val += s
        return self.helper(root.left, root.val)
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, 0)
        return root
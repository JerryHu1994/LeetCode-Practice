# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findHeight(self, root):
        if root == None:    return 0
        return max(self.findHeight(root.left), self.findHeight(root.right)) + 1
    
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == None and root.right == None:    return root.val
        left_height = self.findHeight(root.left)
        right_height = self.findHeight(root.right)
        if left_height >= right_height:
            return self.findBottomLeftValue(root.left)
        else:
            return self.findBottomLeftValue(root.right)
        
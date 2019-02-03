# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, left, right):
        if (left==None and right!=None) or (left!=None and right==None):    return False
        if (left==None and right==None):    return True
        return (left.val==right.val) and self.helper(left.right,right.left) and self.helper(left.left, right.right)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:  return True
        return self.helper(root.left, root.right)
            
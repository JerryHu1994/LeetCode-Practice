# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None:  return root
        if root == p or root == q:  return root
        l, r = self.lowestCommonAncestor(root.left, p, q),self.lowestCommonAncestor(root.right, p, q)
        if l!=None and r==None: return l
        if l==None and r!=None: return r
        if l==None and r==None: return None
        return root
        
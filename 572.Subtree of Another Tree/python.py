# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def isSameTree(self, l, r):
        if l == None and r == None: return True
        if l == None or r == None:  return False
        return l.val == r.val and self.isSameTree(l.left, r.left) and self.isSameTree(l.right, r.right)
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None and t == None: return True
        if s == None or t == None:  return False
        return (s.val == t.val and self.isSameTree(s,t)) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

class Solution:
    def preorder(self, tree):
        if not tree:    return "N"
        return "#" + str(tree.val) + self.preorder(tree.left) + self.preorder(tree.right)
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.preorder(t) in self.preorder(s)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def serialize(self,root):
        if root== None: return "#"
        tree = str(root.val)+self.serialize(root.left)+self.serialize(root.right)
        self.c[tree] += 1
        if tree == "#00":   print "hhh"
        if self.c[tree] == 2:
            self.ret.append(root)
        return tree
    
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.c = collections.Counter()
        self.ret = []
        self.serialize(root)
        return self.ret
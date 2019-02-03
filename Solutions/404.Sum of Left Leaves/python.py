# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root):
        if root == None:
            return
        l = root.left
        if l != None:
            if l.left == None and l.right == None:
                self.ret += l.val
            else:
                self.helper(root.left)
        self.helper(root.right)
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.helper(root)
        return self.ret
        
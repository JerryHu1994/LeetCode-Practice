# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        if self.first == None and self.prenum.val >= root.val:
            self.first = self.prenum
        if self.first != None and self.prenum.val >= root.val:
            self.second = root
        self.prenum = root
        self.inorder(root.right)
        
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first, self.second = None, None
        self.prenum = TreeNode(float("-inf"))
        self.inorder(root)
        self.first.val,self.second.val = self.second.val,self.first.val
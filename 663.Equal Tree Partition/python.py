# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def calSum(self, root):
        if root == None:    return 0
        return root.val + self.calSum(root.left) + self.calSum(root.right)
    
    def helper(self,root):
        if root == None:    return None
        leftsum = self.helper(root.left)
        rightsum = self.helper(root.right)
        if leftsum != None and leftsum == self.totalsum - leftsum:  
            self.ret = True
        if rightsum != None and rightsum == self.totalsum - rightsum:  
            self.ret = True
        retsum = root.val
        if leftsum != None:
            retsum += leftsum
        if rightsum != None:
            retsum += rightsum
        return retsum
            
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.totalsum = self.calSum(root)
        self.ret = False
        self.helper(root)
        return self.ret
        
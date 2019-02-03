# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, root):
        if root == None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
    
    def helper(self,root, height, left, right):
        if height >= len(self.arr) or root==None:
            return
        # set the root val
        mid = (left+right)/2
        self.arr[height][mid] = str(root.val)
        self.helper(root.left, height+1, left, mid-1)
        self.helper(root.right, height+1, mid+1, right)
        
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = self.getHeight(root)
        width = 2**height - 1
        # initialize
        self.arr = [[""]*width for i in range(height)]
        self.helper(root, 0, 0, width-1)
        return self.arr
        
        
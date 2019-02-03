# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # given an inorder, return the treenode
    def helper(self, inorder):
        if len(inorder) == 0:
            return None
        rootval = self.postorder.pop()
        # create the root node
        root = TreeNode(rootval)
        root.right = self.helper(inorder[inorder.index(rootval)+1:])
        root.left = self.helper(inorder[:inorder.index(rootval)])
        return root
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.postorder = postorder # keeps as a static variable
        return self.helper(inorder)
        
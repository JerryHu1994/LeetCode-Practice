# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, inorder):
        if len(self.preorder) == 0 or len(inorder) == 0:
            return None
        rootval = self.preorder[0]
        root = TreeNode(rootval)
        rootidx = inorder.index(rootval)
        self.preorder = self.preorder[1:]
        leftnode = self.helper(inorder[:rootidx])
        rightnode = self.helper(inorder[rootidx+1:])
        root.left, root.right = leftnode, rightnode
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        return self.helper(inorder)
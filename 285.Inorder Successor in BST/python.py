# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root == None:    return None
        # the root is p, found next inorder
        if root.val == p.val:
            curr = root.right
            while curr and curr.left != None:    curr = curr.left
            return curr
        # explore left
        if p.val < root.val:   
            left = self.inorderSuccessor(root.left, p)
            return root if left == None else left
        return self.inorderSuccessor(root.right, p)
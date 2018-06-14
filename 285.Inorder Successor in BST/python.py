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
        if root == None:
            return None
        if p.val == root.val:
            if root.right == None:
                return None
            else:
                curr = root.right
                while curr.left != None:
                    curr = curr.left
                return curr
        if p.val < root.val:
            ret = self.inorderSuccessor(root.left, p)
            if ret == None:
                return root
        else:
            ret = self.inorderSuccessor(root.right, p)
        return ret
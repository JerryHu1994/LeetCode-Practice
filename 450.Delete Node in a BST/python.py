# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:    return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # find the node
            # both left and right node exists
            if root.left != None and root.right != None:
                curr = root.right
                while curr.left != None:    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
            else:
                root = root.left if root.left != None else root.right
        return root
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None and root2 == None: return True
        if root1 == None or root2 == None:  return False
        if root1.val != root2.val:  return False
        # not switch
        print root1.val, root2.val
        if ((root1.left == None and root2.left == None) or (root1.left != None and root2.left != None and root1.left.val == root2.left.val)) and ((root1.right == None and root2.right == None) or (root1.right != None and root2.right != None and root1.right.val == root2.right.val)):
            res = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            if res: return True
        # switch
        if ((root1.left == None and root2.right == None) or (root1.left != None and root2.right != None and root1.left.val == root2.right.val)) and ((root1.right == None and root2.left == None) or (root1.right != None and root2.left != None and root1.right.val == root2.left.val)):
            res = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
            if res: return True
        return False
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countHeight(self, root):
        count, curr = 0, root
        while curr != None:
            curr = curr.left
            count += 1
        return count
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:    return 0
        ret = 0
        leftdepth, rightdepth = self.countHeight(root.left), self.countHeight(root.right)
        if leftdepth == rightdepth:
            ret += 2**leftdepth
            ret += self.countNodes(root.right)
        else:
            ret += 2**rightdepth
            ret += self.countNodes(root.left)
        return ret
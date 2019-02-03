# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:
            return None, 0
        leftnum, leftlen = self.helper(root.left)
        rightnum, rightlen = self.helper(root.right)
        l = 1
        if leftnum != None and root.val == leftnum - 1:
            l = max(l, leftlen + 1)
        if rightnum != None and root.val == rightnum - 1:
            l = max(l, rightlen + 1)
        self.ret = max(l, self.ret)
        return root.val, l
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.helper(root)
        return self.ret
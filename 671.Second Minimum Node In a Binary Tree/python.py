# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:    return
        self.set.add(root.val)
        self.helper(root.left)
        self.helper(root.right)
    
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.set = set()
        self.helper(root)
        ret = sorted(list(self.set))
        return ret[1] if len(ret) >= 2 else -1
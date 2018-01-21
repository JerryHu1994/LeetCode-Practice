# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root==None:  return []
        if root.left==None and root.right==None:
            return [[root.val]] if sum==root.val else []
        ret = []
        if root.left!=None:
            leftret = self.pathSum(root.left, sum-root.val)
            ret = ret + [[root.val]+i for i in leftret]
        if root.right!=None:
            rightret = self.pathSum(root.right, sum-root.val)
            ret = ret+[[root.val]+i for i in rightret]
        return ret
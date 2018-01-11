# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:    return []
        if root.left==None and root.right==None:    return [str(root.val)]
        l = self.binaryTreePaths(root.left)  if root.left!=None else []
        r = self.binaryTreePaths(root.right) if root.right!=None else []
        ret = []
        for i in l+r:
            ret.append(str(root.val)+"->"+i)
        return ret
        
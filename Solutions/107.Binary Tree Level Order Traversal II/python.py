# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:  return []
        ret = []
        currlevel = [root]
        nextlevel = []
        while len(currlevel):
            ret.append([i.val for i in currlevel])
            for i in currlevel:
                if i.left != None:  nextlevel.append(i.left)
                if i.right != None:  nextlevel.append(i.right)
            currlevel = nextlevel
            nextlevel = []
        return ret[::-1]
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:
            return -1
        level = max(self.helper(root.left), self.helper(root.right)) + 1
        while len(self.ret) <= level:
            self.ret.append([])
        self.ret[level].append(root.val)
        return level
    
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ret = []
        self.helper(root)
        return self.ret
                        
                
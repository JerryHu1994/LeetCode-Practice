# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def helper(self, root):
        if root == None:    return []
        left = self.helper(root.left)
        right = self.helper(root.right)
        if not len(left) and not len(right):
            self.ret += root.val
            return [1]
        lens = left + right
        for i in lens:
            self.ret += int(math.pow(10,i))*root.val
        updated_lens = [i+1 for i in lens]
        return updated_lens
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.helper(root)
        return self.ret
            
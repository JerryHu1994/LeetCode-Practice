# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:
            return 0, 0
        curr_inc, curr_dec = 1, 1
        left_inc, left_dec = self.helper(root.left)
        if root.left != None:
            if root.left.val + 1 == root.val:
                curr_inc = max(left_inc+1, curr_inc)
            if root.left.val - 1 == root.val:
                curr_dec = max(left_dec+1, curr_dec)
        right_inc, right_dec = self.helper(root.right)
        if root.right != None:
            if root.right.val + 1 == root.val:
                curr_inc = max(right_inc+1, curr_inc)
            if root.right.val - 1 == root.val:
                curr_dec = max(right_dec+1, curr_dec) 
        self.ret = max(curr_inc + curr_dec - 1, self.ret)
        print curr_inc, curr_dec, root.val
        return curr_inc, curr_dec
    
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        self.helper(root)
        return self.ret
        
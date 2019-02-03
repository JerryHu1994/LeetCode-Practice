# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, findmode):
        if root == None:    return
        self.helper(root.left, findmode)
        
        if root.val != self.curr_val:
            self.curr_val = root.val
            self.curr_count = 0
        self.curr_count += 1
        
        if self.curr_count > self.mode_count:
            self.mode_count = self.curr_count
        elif self.curr_count == self.mode_count and not findmode:
            self.ret.append(root.val)
            
        self.helper(root.right, findmode)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        self.curr_val = None
        self.curr_count = 0
        self.mode_count = 0
        self.helper(root, True)
        self.curr_val = None
        self.curr_count = 0
        self.helper(root, False)
        return self.ret
        
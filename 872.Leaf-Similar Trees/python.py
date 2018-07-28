# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def helper(self, root):
        leaves = []
        stack = [root]
        while len(stack):
            curr = stack.pop()
            if curr.left == None and curr.right == None:
                leaves.append(curr.val)
                continue
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)
        return leaves
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        l1 = self.helper(root1)
        l2 = self.helper(root2)
        
        if len(l1) != len(l2):  return False
        for i in range(len(l1)):
            if l1[i] != l2[i]:  return False
        return True
        
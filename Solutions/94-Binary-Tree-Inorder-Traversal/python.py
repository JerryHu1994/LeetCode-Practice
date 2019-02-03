# Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right

# Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, ret, curr = [], [], root
        while curr != None:
            stack.append(curr)
            curr = curr.left
        
        while len(stack):
            p = stack.pop()
            ret.append(p.val)
            # check if p has right
            r = p.right
            # add linear left of r
            while r != None:
                stack.append(r)
                r = r.left
        return ret
            
            
        
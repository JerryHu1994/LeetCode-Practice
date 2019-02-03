# Recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:    return
        self.ret.append(root.val)
        self.helper(root.left)
        self.helper(root.right)
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        self.helper(root)
        return self.ret

# Iterative
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:  return []
        stack, ret = [root], []
        while len(stack):
            curr = stack.pop()
            ret.append(curr.val)
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)
        return ret
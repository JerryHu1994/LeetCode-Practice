# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:    return []
        stack = [root]
        ret = []
        while len(stack):
            curr = stack.pop()
            ret.append(curr.val)
            if curr.left != None:   stack.append(curr.left)
            if curr.right != None:   stack.append(curr.right)
        return ret[::-1]
        
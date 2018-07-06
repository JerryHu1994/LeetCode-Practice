# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        ret = []
        stack = [(root, 0)]
        while len(stack):
            node, depth = stack.pop()
            if node.left != None:   
                stack.append((node.left, depth+1))
            if node.right != None:  
                stack.append((node.right, depth+1))
            if depth >= len(ret):
                ret.append(node.val)
        return ret
            
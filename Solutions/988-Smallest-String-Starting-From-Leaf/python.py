# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root == None:    return ""
        self.ans = None
        f = lambda s:"".join([chr(ord('a')+i) for i in s])[::-1]
        def dfs(node, prepath):
            if node.left == None and node.right == None:
                string = f(prepath)
                if self.ans == None or string < self.ans:    self.ans = string
                return
            if node.left:
                dfs(node.left, prepath+[node.left.val])
            if node.right:
                dfs(node.right, prepath+[node.right.val])
        dfs(root, [root.val])
        return self.ans
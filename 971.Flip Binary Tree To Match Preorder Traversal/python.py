# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.ans = []
        self.ind = 0
        def dfs(node):
            if node == None:    return
            if node.val != voyage[self.ind]:
                self.ans = [-1]
                return
            self.ind += 1
            if self.ind < len(voyage) and node.left and node.left.val != voyage[self.ind]:
                self.ans.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.ans
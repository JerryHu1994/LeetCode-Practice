# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N%2 == 0:    return []
        if N == 1:  return [TreeNode(0)]
        n = N-1
        ret = []
        for i in range(n):
            if i%2 == 1 and (n-i) %2 == 1:
                left_trees, right_trees = self.allPossibleFBT(i), self.allPossibleFBT(n-i)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(0)
                        root.left, root.right = l,r
                        ret.append(root)
        return ret
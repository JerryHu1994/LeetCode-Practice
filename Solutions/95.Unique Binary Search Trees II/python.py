# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, interval):
        left, right = interval
        if interval in self.dic:
            return self.dic[interval]
        if left > right:
            return [None]
        ret = []
        for i in range(left, right+1):
            left_trees = self.helper((left, i-1))
            right_trees = self.helper((i+1, right))
            # construct tree based on left tree and right tree
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(i)
                    root.left, root.right = l, r
                    ret.append(root)
        # save to dic
        self.dic[interval] = ret
        return ret
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:    return []
        self.dic = {}
        return self.helper((1,n))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = collections.defaultdict(list)
        def dfs(node, x, y):
            if node == None:    return
            dic[x].append((y, node.val))
            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)
        dfs(root, 0, 0)
        ans = []
        keys = sorted([k for k in dic.keys()])
        for k in keys:
            ans.append([v[1]    for v in sorted(dic[k])])
        return ans
            
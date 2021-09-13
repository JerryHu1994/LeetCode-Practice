# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def helper(node):
            if node == None:    return []
            return helper(node.left) + [node.val] + helper(node.right)
        root_list = helper(root)
        root_list.append(val)
        def construct(li):
            if len(li) == 0:    return None
            max_val = max(li)
            max_index = li.index(max_val)
            r = TreeNode(max_val)
            r.left, r.right = construct(li[:max_index]), construct(li[max_index+1:])
            return r
        return construct(root_list)
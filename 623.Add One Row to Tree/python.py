# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newroot = TreeNode(v)
            newroot.left = root
            return newroot
        queue, nextq = [root], []
        for i in range(d-2):
            for node in queue:
                if node.left != None:   nextq.append(node.left)
                if node.right != None:  nextq.append(node.right)
            queue, nextq = nextq, []
        for node in queue:
            left_child, right_child = TreeNode(v), TreeNode(v)
            left_child.left, right_child.right = node.left, node.right
            node.left, node.right = left_child, right_child
        return root
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root == None:    return False
        queue = [root]
        while len(queue):
            nextqueue = []
            parents = {}
            s = set()
            for node in queue:
                if node.left:
                    s.add(node.left.val)
                    parents[node.left.val] = node
                    nextqueue.append(node.left)
                if node.right:
                    s.add(node.right.val)
                    parents[node.right.val] = node
                    nextqueue.append(node.right)
            if x in s and y in s and parents[x] != parents[y]:
                return True
            elif x in s or y in s:
                return False
            queue = nextqueue
        return False
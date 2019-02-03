# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:    return True
        level, curr = 0, root
        while curr != None:
            level += 1
            curr = curr.left
        queue = [root]
        currlevel = 0
        while len(queue):
            size, nextq = len(queue), []
            if currlevel < level-1:
                queue = [n  for n in queue if n != None]
                if len(queue) != 2**currlevel:  return False
            elif currlevel == level-1:
                while queue[-1] == None:    queue.pop()
                if None in queue:   return False
            else:
                queue = [n  for n in queue if n != None]
                if len(queue):  return False
            for n in queue:
                nextq.append(n.left)
                nextq.append(n.right)
            queue = nextq
            currlevel += 1
        return True
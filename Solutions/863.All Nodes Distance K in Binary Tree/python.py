# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        parents = {}
        queue = [root]
        targetnode = None
        while len(queue):
            curr = queue.pop(0)
            if curr == target:
                targetnode = curr
                break
            if curr.left != None:
                queue.append(curr.left)
                parents[curr.left] = curr
            if curr.right != None:
                queue.append(curr.right)
                parents[curr.right] = curr
        currlevel, nextlevel, visited = [target], [], set()
        for i in range(K):
            while len(currlevel):
                c = currlevel.pop()
                visited.add(c)
                # append parent if exists
                if c in parents and parents[c] not in visited:
                    nextlevel.append(parents[c])
                # append left and right node
                if c.left != None and c.left not in visited:
                    nextlevel.append(c.left)
                if c.right != None and c.right not in visited:
                    nextlevel.append(c.right)
            currlevel, nextlevel = nextlevel, []
        return [i.val for i in currlevel]
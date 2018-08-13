# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def reverse(self, root, k):
        if root.val == k:   return root
        if root.left:
            self.reversemap[root.left] = root
            ret = self.reverse(root.left, k)
            if ret: return ret
        if root.right:
            self.reversemap[root.right] = root
            ret = self.reverse(root.right, k)
            if ret: return ret
        return None
    
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.reversemap = {}
        knode = self.reverse(root, k)
        queue = [knode]
        visited = set([k])
        while len(queue):
            curr = queue.pop(0)
            if curr.left == None and curr.right == None:    return curr.val
            if curr.left != None and curr.left.val not in visited:
                visited.add(curr.left.val)
                queue.append(curr.left)
            if curr.right != None and curr.right.val not in visited:
                visited.add(curr.right.val)
                queue.append(curr.right)
            if curr in self.reversemap and self.reversemap[curr].val not in visited:
                visited.add(self.reversemap[curr].val)
                queue.append(self.reversemap[curr])
        return -1
    
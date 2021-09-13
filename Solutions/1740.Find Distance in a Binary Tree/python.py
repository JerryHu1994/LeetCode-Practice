# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def lca(node, p, q):
            if node == None:    return None
            lnode = lca(node.left, p, q)
            rnode = lca(node.right, p, q)
            
            if node.val == p or node.val == q:
                return node
            
            if lnode != None and rnode != None:
                return node
            if lnode != None:
                return lnode
            if rnode != None:
                return rnode
        def findDepth(node, num, depth):
            if node is None:    return None
            if node.val == num: return depth
            lres = findDepth(node.left, num, depth+1)
            if lres != None:    return lres
            rres = findDepth(node.right, num, depth+1)
            if rres != None:    return rres
            
        lowest_root = lca(root, p, q)
        return findDepth(lowest_root, q, 0) + findDepth(lowest_root, p, 0)
        
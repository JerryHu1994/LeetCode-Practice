# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        isLeaf = lambda node : node.left == None and node.right == None
        if root == None:    return []
        if isLeaf(root):   return [root.val]
        leaves = []
        curr, left = root.left, []
        # append left boundary
        while curr != None and not isLeaf(curr):
            left.append(curr.val)
            curr = curr.left if curr.left else curr.right
        # append leaves
        def addLeaves(node):
            if isLeaf(node):
                leaves.append(node.val)
                return
            if node.left:   addLeaves(node.left)
            if node.right:   addLeaves(node.right)
        addLeaves(root)
        # append right boundary
        curr, right = root.right, []
        while curr != None and not isLeaf(curr):
            right.append(curr.val)
            curr = curr.right if curr.right else curr.left
        return [root.val] + left + leaves + right[::-1]
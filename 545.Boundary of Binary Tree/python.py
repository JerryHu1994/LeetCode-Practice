# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isLeaf(self, node):
        return node.left==None and node.right==None
    
    def addLeaves(self, node):
        if self.isLeaf(node):
            self.leaves.append(node.val)
        if node.left:   self.addLeaves(node.left)
        if node.right:  self.addLeaves(node.right)
    
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:    return []
        if self.isLeaf(root):   return [root.val]
        self.leaves = []
        curr = root.left
        left = []
        # append left boundary
        while curr != None and not self.isLeaf(curr):
            left.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        # append leaves
        self.addLeaves(root)
        #append right boundary
        right = []
        curr = root.right
        while curr != None and not self.isLeaf(curr):
            right.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        return [root.val] + left + self.leaves + right[::-1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left == None and root.right == None:
            if root.val == target:
                print ("removing")
                return None
            else:
                return root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left == None and root.right == None:
            if root.val == target:
                print ("removing")
                return None
        return root
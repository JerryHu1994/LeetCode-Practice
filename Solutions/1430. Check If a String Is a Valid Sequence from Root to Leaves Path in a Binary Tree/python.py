# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        if root == None:    return False
        if root.left == None and root.right == None and len(arr) == 1 and arr[0] == root.val:
            return True
        if len(arr) != 0:
            if root.val != arr[0]:
                return False
            else:
                if self.isValidSequence(root.left, arr[1:]):    return True
                if self.isValidSequence(root.right, arr[1:]):   return True
        else:
            return False
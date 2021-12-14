# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        rootval = preorder[0]
        root = TreeNode(rootval)
        ind = 1
        while ind < len(preorder) and preorder[ind] < rootval:
            ind += 1
        root.left = self.bstFromPreorder(preorder[1:ind])
        root.right = self.bstFromPreorder(preorder[ind:])
        return root
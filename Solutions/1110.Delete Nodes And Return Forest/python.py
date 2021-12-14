# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete_set = set(to_delete)
        def deletenode(root, isroot):
            if root == None:    return
            if root.val in to_delete_set:
                deletenode(root.left, True)
                deletenode(root.right, True)
                return
            else:
                if root.left != None:
                    if root.left.val in to_delete_set:
                        deletenode(root.left, True)
                        root.left = None
                    else:
                        deletenode(root.left, False)
                if root.right != None:
                    if root.right.val in to_delete_set:
                        deletenode(root.right, True)
                        root.right = None
                    else:
                        deletenode(root.right, False)
            if isroot:
                ans.append(root)
        deletenode(root, True)
        return ans
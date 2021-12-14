# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def search(node, flag):
            if flag:
                self.ans.append(node.val)
            if node.left == None:
                if node.right != None:
                    search(node.right, True)
            else:
                if node.right != None:
                    search(node.right, False)
            if node.right == None:
                if node.left != None:
                    search(node.left, True)
            else:
                if node.left != None:
                    search(node.left, False)
        if root != None:
            search(root, False)
        return self.ans
        
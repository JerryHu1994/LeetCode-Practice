# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        set1 = set()
        def search(rootnode):
            if rootnode != None:
                set1.add(rootnode.val)
                if rootnode.left != None:
                    search(rootnode.left)
                if rootnode.right != None:
                    search(rootnode.right)
        search(root1)
        if root2 == None:   return False
        queue2 = [root2]
        while len(queue2):
            curr = queue2.pop(0)
            if target - curr.val in set1:
                return True
            if curr.left != None:
                queue2.append(curr.left)
            if curr.right != None:
                queue2.append(curr.right)
        return False
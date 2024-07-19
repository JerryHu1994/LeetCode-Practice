# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:    return None
        stack, cul_sum = [root], 0
        currnode = root
        while currnode.right != None:
            currnode = currnode.right
            stack.append(currnode)
        while len(stack):
            curr = stack.pop()
            curr.val = curr.val + cul_sum
            cul_sum = curr.val
            if curr.left != None:
                currptr = curr.left
                stack.append(currptr)
                while currptr.right != None:
                    currptr = currptr.right
                    stack.append(currptr)
        return root
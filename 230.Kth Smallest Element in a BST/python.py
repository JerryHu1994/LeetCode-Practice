# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack, ptr, count = [root], root, 0
        while len(stack):
            if ptr!=None:
                stack.append(ptr)
                ptr = ptr.left
            else:
                curr = stack.pop()
                count += 1
                if count==k:    return curr.val
                ptr = curr.right
        return 0
        
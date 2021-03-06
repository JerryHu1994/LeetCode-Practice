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
        stack, count, curr = [], 0, root
        while True:
            if curr!= None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                count+=1
                if count==k:    return curr.val
                curr = curr.right
                
                
        
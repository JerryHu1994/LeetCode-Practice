# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        ret = [root.val]
        stack = [root]
        nextstack = []
        while True:
            curr = stack.pop()
            if curr.left != None:   nextstack.append(curr.left)
            if curr.right != None:  nextstack.append(curr.right)
            if len(stack) == 0: 
                if len(nextstack) == 0: break
                ret.append(max([i.val for i in nextstack]))
                stack = nextstack
                nextstack = []
        return ret
            
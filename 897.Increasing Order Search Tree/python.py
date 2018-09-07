# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        curr = root
        while curr != None:
            stack.append(curr)
            curr = curr.left
        ret = []
        while len(stack):
            toadd = stack.pop()
            if toadd.right != None:
                curr = toadd.right
                while curr != None:
                    stack.append(curr)
                    curr = curr.left
            ret.append(toadd)
        retroot = currroot = TreeNode(0)
        for i in range(len(ret)):
            currroot.right = ret[i]
            currroot = currroot.right
            currroot.left = None
        return retroot.right
        
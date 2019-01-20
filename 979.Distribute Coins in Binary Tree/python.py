# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:    return 0
        self.count = {}
        def count(node):
            if node == None:   return 0, 0
            lcount, lval = count(node.left)
            rcount, rval = count(node.right)
            self.count[node] = (lcount+1+rcount, lval+node.val+rval)
            return self.count[node]
        count(root)
        self.ans = 0
        def helper(node):
            if node == None:    return 0
            helper(node.left)
            helper(node.right)
            l = self.count[node.left] if node.left else 0
            r = self.count[node.right] if node.right else 0
            if l:   l = l[1]-l[0]
            if r:   r = r[1]-r[0]
            mid = node.val
            inc = abs(l)+abs(r)
            self.ans += inc
            return l+r+mid-1
        helper(root)
        return self.ans
            
            
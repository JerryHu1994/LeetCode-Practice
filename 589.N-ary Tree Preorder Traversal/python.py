# Recrusive solution
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def helper(self, root):
        if root==None:
            return
        self.ret.append(root.val)
        childs = root.children
        for i in childs:
            self.helper(i)
        
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root==None:
            return []
        self.ret = []
        self.helper(root)
        return self.ret
                
# Iterative Solution
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root==None:
            return []
        ret = []
        stack = [root]
        while len(stack):
            curr = stack.pop()
            ret.append(curr.val)
            childrens = [i for i in curr.children][::-1]
            for c in childrens:
                stack.append(c)
        return ret
        
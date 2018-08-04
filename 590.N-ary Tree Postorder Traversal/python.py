# Recursive
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def helper(self, root):
        if root == None:
            return
        for i in root.children:
            self.helper(i)
        self.ret.append(root.val)
    
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.ret = []
        self.helper(root)
        return self.ret
# Iterative
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        queue = [root]
        ret = []
        while len(stack):
            curr = queue.pop()
            ret.append(curr.val)
            for i in curr.children:
                stack.append(i)
        return ret[::-1]
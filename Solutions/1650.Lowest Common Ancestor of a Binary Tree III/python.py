"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if p.parent == None:    return p
        dic = {}
        curr = q
        while curr != None:
            if curr.val == p.val:   return p
            dic[curr.val] = curr
            curr = curr.parent
        curr = p
        while curr != None:
            if curr.val in dic: return dic[curr.val]
            curr = curr.parent
        return curr
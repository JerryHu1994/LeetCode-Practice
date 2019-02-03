"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:    return []
        prelevel = [root]
        postlevel = []
        ret = []
        while True:
            currlevel = []
            while len(prelevel):
                curr = prelevel.pop(0)
                currlevel.append(curr.val)
                for i in curr.children:
                    postlevel.append(i)
            ret.append(currlevel)
            prelevel = postlevel
            postlevel = []
            if len(prelevel) == 0:
                break
        return ret
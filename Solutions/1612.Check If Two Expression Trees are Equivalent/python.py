# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def explore_tree(root, currlist):
            if root.left != None:
                explore_tree(root.left, currlist)
                explore_tree(root.right, currlist)
            else:
                currlist[root.val] += 1
        leftlist, rightlist = defaultdict(int), defaultdict(int)
        explore_tree(root1, leftlist)
        explore_tree(root2, rightlist)
        for key1 in leftlist:
            if key1 not in rightlist or rightlist[key1] != leftlist[key1]:
                return False
        for key2 in rightlist:
            if key2 not in leftlist or rightlist[key2] != leftlist[key2]:
                return False
        return True
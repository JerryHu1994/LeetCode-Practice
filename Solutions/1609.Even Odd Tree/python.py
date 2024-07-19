# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def checkIncreasing(li: List[int]):
            for n in li:
                if n%2 != 1:    return False
            for i in range(len(li)-1):
                if li[i] >= li[i+1]: return False
            return True
        def checkDecreasing(li: List[int]):
            for n in li:
                if n%2 !=0: return False
            for i in range(len(li)-1):
                if li[i] <= li[i+1]: return False
            return True
        queue = [root]
        currlevel = 0
        while len(queue):
            nextq = []
            if currlevel % 2 == 0:
                if not checkIncreasing([n.val for n in queue]):
                    return False
            else:
                if not checkDecreasing([n.val for n in queue]):
                    return False
            for n in queue:
                if n.left != None:  nextq.append(n.left)
                if n.right != None:  nextq.append(n.right)
            queue = nextq
            currlevel += 1
        return True
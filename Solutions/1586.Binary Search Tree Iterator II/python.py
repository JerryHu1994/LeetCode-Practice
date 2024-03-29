# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.previousarr = []
        self.idx = -1
        curr = root
        while curr != None:
            self.stack.append(curr)
            curr = curr.left

    def hasNext(self) -> bool:
        return self.idx < len(self.previousarr)-1 or len(self.stack) != 0

    def next(self) -> int:
        if self.idx < len(self.previousarr)-1:
            self.idx += 1
            return self.previousarr[self.idx]
        curr = self.stack.pop()
        nextnode = curr.right
        while nextnode != None:
            self.stack.append(nextnode)
            nextnode = nextnode.left
        self.previousarr.append(curr.val)
        self.idx += 1
        return curr.val

    def hasPrev(self) -> bool:
        return self.idx > 0

    def prev(self) -> int:
        self.idx -= 1
        return self.previousarr[self.idx]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()